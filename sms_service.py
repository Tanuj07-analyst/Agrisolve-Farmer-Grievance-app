import requests

def send_ticket_sms(to_phone_number, farmer_name, ticket_details):
    """
    Real SMS Notification Service using Textbee API Key
    """
    # 1.API Key for Textbee (Replace with your actual API key)
    TEXTBEE_API_KEY = "txb_Uh1HhGUidfLouXSrb8I2dYVRyUvx4q1g"  # Replace with your actual Textbee API key
    
    # 2. Number Format Fix (+91 handling)
    clean_number = str(to_phone_number).strip().replace("+", "")
    if not clean_number.startswith("91"):
        clean_number = "91" + clean_number
    
    formatted_phone = "+" + clean_number

    # 3. Message Body
    sms_text = (
        f"Namaste {farmer_name if farmer_name else 'Kisan Bhai'}, "
        f"Aapki Grievance Ticket generate ho gayi hai. "
        f"Ticket ID: {ticket_details['ticket_id']}, "
        f"Dept: {ticket_details['department']}, "
        f"Priority: {ticket_details['priority']}. - AgriSolve Portal"
    )

    url = "https://api.textbee.dev/api/v1/gateway/send-sms"
    
    headers = {
        "x-api-key": TEXTBEE_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "recipients": [formatted_phone],
        "message": sms_text
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code in [200, 201]:
            return True, "SMS Dispatched successfully via Mobile Gateway!"
        else:
            return False, f"Textbee Error: {response.status_code} - {response.text}"

    except Exception as e:
        return False, f"Gateway Network Error: {str(e)}"