def get_chatbot_response(user_message):

    message = user_message.lower()

    # Development field
    if "development" in message or "developer" in message:
        if "10" in message or "12" in message:
            return "You can become a Web Developer or Software Developer. Average salary: 6-15 LPA."
        else:
            return "You can explore careers like Software Developer, App Developer, or Backend Developer."

    # Design field
    elif "design" in message:
        return "You can become a Graphic Designer or UI/UX Designer. Salary range: 4-12 LPA."

    # Business field
    elif "business" in message:
        return "You can become a Business Analyst or Entrepreneur. Salary range: 6-20 LPA."

    # Data field
    elif "data" in message:
        return "You can become a Data Scientist or Data Analyst. Salary range: 8-25 LPA."

    # Content field
    elif "content" in message or "youtube" in message:
        return "You can become a Content Creator or Digital Marketer."

    else:
        return "Please tell me your interest field (development, data, design, business, content)."
