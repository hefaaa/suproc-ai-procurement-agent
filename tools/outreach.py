class OutreachGenerator:

    def generate(self, suppliers, requirement):

        messages = []

        for supplier in suppliers:

            message = f"""
To: {supplier['CompanyName']}

Subject: Procurement Enquiry

Hello,

We are looking for biodegradable containers.

Requirement

• Quantity : {requirement.min_capacity}

• Delivery : within {requirement.max_delivery_days} days

Please share

• Pricing

• Availability

• Lead time

Regards

Business Procurement Team
"""

            messages.append(message)

        return messages