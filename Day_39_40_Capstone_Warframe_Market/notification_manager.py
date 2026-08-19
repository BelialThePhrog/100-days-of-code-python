import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.email = os.getenv("SMTP_EMAIL")
        self.password = os.getenv("SMTP_PASSWORD")
        self.host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.port = int(os.getenv("SMTP_PORT", 587))

    def build_email_content(self, user_name: str, matched_items: List[Dict], unmatched_items: List[Dict]) -> Tuple[str, str]:
        """
        Builds both plain text and HTML summary bodies.
        """
        total_found = len(matched_items)
        subject_status = "Deals Found!" if total_found > 0 else "No Matching Deals Right Now"

        # --- Plain Text Version ---
        text_lines = [f"Hi {user_name}!", "", f"Status: {subject_status} ({total_found} deals below target)", ""]
        if matched_items:
            text_lines.append("=== AVAILABLE DEALS ===")
            for deal in matched_items:
                text_lines.append(f"• Item: {deal['name']}")
                text_lines.append(f"  Target Price: {deal['target_price']} pl | Best In-Game Price: {deal['current_price']} pl")
                text_lines.append(f"  Seller: {deal['seller']}")
                text_lines.append(f"  In-Game Chat Whisper:")
                text_lines.append(f"  {deal['whisper']}")
                text_lines.append("-" * 40)

        if unmatched_items:
            text_lines.append("\n=== STILL SEARCHING ===")
            for item in unmatched_items:
                text_lines.append(f"• {item['name']} - Lowest In-Game: {item.get('lowest', 'N/A')} pl (Target: {item['target_price']} pl)")

        # --- HTML Version ---
        html_deals = ""
        for deal in matched_items:
            html_deals += f"""
            <div style="margin-bottom: 20px; padding: 15px; border-left: 4px solid #2ecc71; background-color: #f9f9f9;">
                <h3 style="margin-top: 0; color: #2c3e50;">{deal['name']}</h3>
                <p><strong>Your Target:</strong> {deal['target_price']} pl | <strong style="color: #27ae60;">Current Best:</strong> {deal['current_price']} pl</p>
                <p><strong>Seller (In-game):</strong> {deal['seller']}</p>
                <p style="margin-bottom: 5px;"><strong>Warframe Chat Command:</strong></p>
                <code style="display: block; background: #272b30; color: #00ffcc; padding: 10px; border-radius: 4px; font-family: monospace;">
                    {deal['whisper']}
                </code>
            </div>
            """

        html_unmatched = "".join([
            f"<li><strong>{item['name']}</strong>: Lowest found {item.get('lowest', 'N/A')} pl (Your target: {item['target_price']} pl)</li>"
            for item in unmatched_items
        ])

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
            <h2>Tenno Market Price Alert Summary</h2>
            <p>Hi <strong>{user_name}</strong>,</p>
            <p><strong>Status:</strong> {subject_status}</p>
            
            {"<h3>Great Deals Found:</h3>" + html_deals if matched_items else "<p>No active in-game listings matched your price constraints today.</p>"}
            
            {f"<h3>Other Tracked Items:</h3><ul>{html_unmatched}</ul>" if unmatched_items else ""}
            <br>
            <p style="font-size: 12px; color: #7f8c8d;">Powered by Warframe Market API & Sheety Capstone.</p>
        </body>
        </html>
        """

        return "\n".join(text_lines), html_body

    def send_notification(self, recipient_email: str, user_name: str, matched: List[Dict], unmatched: List[Dict]) -> bool:
        text_content, html_content = self.build_email_content(user_name, matched, unmatched)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Warframe Market Alert: {len(matched)} Deal(s) Found!"
        msg["From"] = self.email
        msg["To"] = recipient_email

        msg.attach(MIMEText(text_content, "plain"))
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            print(f"[OK] Notification sent successfully to {recipient_email}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to send email to {recipient_email}: {e}")
            return False