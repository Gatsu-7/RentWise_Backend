# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pdfkit  # Install using `pip install pdfkit`

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend-backend communication

# @app.route("/generate-agreement", methods=["POST"])
# def generate_agreement():
#     data = request.json
#     agreement_text = generate_mock_agreement(data)  # Use your own logic
#     return jsonify({"agreementText": agreement_text})

# @app.route("/download-pdf", methods=["POST"])
# def download_pdf():
#     data = request.json
#     agreement_text = data.get("agreementText", "")

#     # Convert text to a simple HTML for PDF generation
#     html_content = f"<html><body><pre>{agreement_text}</pre></body></html>"
    
#     pdf_path = "rental_agreement.pdf"
#     pdfkit.from_string(html_content, pdf_path)

#     return send_file(pdf_path, as_attachment=True)

# def generate_mock_agreement(data):
#     return f"Rental Agreement for {data.get('tenantName')} with {data.get('landlordName')}."

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
CORS(app) 

@app.route("/generate-agreement", methods=["POST"])
def generate_agreement():
    data = request.json
    agreement_text = generate_mock_agreement(data) 
    return jsonify({"agreementText": agreement_text})

@app.route("/download-pdf", methods=["POST"])
def download_pdf():
    data = request.json
    agreement_text = data.get("agreementText", "")

    pdf_path = "rental_agreement.pdf"
    generate_pdf(agreement_text, pdf_path)

    return send_file(pdf_path, as_attachment=True)


# def generate_mock_agreement(data):
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <style>
#             body {{
#                 font-family: 'Segoe UI', Arial, sans-serif;
#                 margin: 40px;
#                 padding: 30px;
#                 line-height: 1.6;
#                 text-align: justify;
#                 color: #333;
#                 background-color: #f9f9f9;
#             }}
#             .container {{
#                 max-width: 800px;
#                 margin: 0 auto;
#                 background-color: white;
#                 padding: 40px;
#                 box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
#                 border-radius: 8px;
#             }}
#             h1 {{
#                 text-align: center;
#                 color: #2c3e50;
#                 font-size: 24px;
#                 margin-bottom: 20px;
#                 font-weight: bold;
#             }}
#             .header-row {{
#                 display: flex;
#                 justify-content: space-between;
#                 margin-bottom: 20px;
#             }}
#             .underline {{
#                 border-bottom: 1px solid #000;
#                 min-width: 200px;
#                 display: inline-block;
#                 margin: 0 5px;
#             }}
#             .paragraph {{
#                 margin-bottom: 20px;
#             }}
#             .signature {{
#                 margin-top: 30px;
#                 text-align: right;
#                 padding-right: 40px;
#             }}
#             .sign-line {{
#                 border-top: 1px solid #000;
#                 display: inline-block;
#                 width: 200px;
#                 margin-bottom: 5px;
#             }}
#             .witness-section {{
#                 margin-top: 40px;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <div class="header-row">
#                 <div>Stamp Rs.</div>
#                 <div>
#                     With No. <span class="underline"></span> 
#                     Date: <span class="underline">{data.get('agreementDate', '________')}</span>
#                 </div>
#             </div>

#             <h1>DEED OF RENT</h1>

#             <div class="paragraph">
#                 This Deed of Rent is made at <span class="underline">{data.get('agreementLocation', '________')}</span>, this <span class="underline">{data.get('agreementDate', '________')}</span> effective from 
#                 <span class="underline">{data.get('startDate', '________')}</span> between <span class="underline">{data.get('landlordName', '________')}</span>,
#                 aged <span class="underline">{data.get('landlordAge', '________')}</span> Years residing at <span class="underline">{data.get('landlordAddress', '________')}</span>, 
#                 hereinafter called the <strong>HOUSE OWNER</strong> of the <strong>ONE PART</strong> and 
#                 <span class="underline">{data.get('tenantName', '________')}</span>, aged <span class="underline">{data.get('tenantAge', '________')}</span> Years residing at 
#                 <span class="underline">{data.get('tenantAddress', '________')}</span>, hereinafter called the 
#                 <strong>TENANT</strong> of the <strong>OTHER PART</strong>.
#             </div>

#             <div class="paragraph">
#                 WHEREAS the House owner is the sole absolute owner of <span class="underline">{data.get('propertyAddress', '________')}</span>.
#             </div>

#             <div class="paragraph">
#                 WHEREAS the tenant has applied to the Houseowner for grant of tenancy for 
#                 the premises situated at the above address for living accommodation.
#             </div>

#             <div class="paragraph">
#                 <strong>NOW THIS DEED OF TENANCY WITNESSETH THE FOLLOWING:</strong>
#             </div>

#             <div class="paragraph">
#                 1. The Tenancy shall be initially for the period of <span class="underline">{data.get('leaseDuration', '________')}</span> months, 
#                 with effect from <span class="underline">{data.get('startDate', '________')}</span> and may be renewed from time to time with mutual 
#                 consent of both parties.
#             </div>

#             <div class="paragraph">
#                 2. The rent payable by the Tenant to the House owner shall be Rs. <span class="underline">{data.get('rentalAmount', '________')}</span> /- 
#                 (<span class="underline">{data.get('rentalAmountWords', '________')}</span> only) per month, payable on or 
#                 before <span class="underline">{data.get('rentDueDate', '________')}</span> of every month.
#             </div>

#             <div class="paragraph">
#                 3. The Tenant has paid a sum of Rs. <span class="underline">{data.get('securityDeposit', '________')}</span>/- (Rupees 
#                 <span class="underline">{data.get('securityDepositWords', '________')}</span> only) as an interest-free rent advance, which 
#                 shall be returned upon vacating the premises after adjustments.
#             </div>

#             <div class="paragraph">
#                 4. The Tenant shall not sublease or sublet any part of the premises, which is strictly for residential purposes only.
#             </div>

#             <div class="paragraph">
#                 5. The House Owner shall be at liberty to inspect the house premises by himself or any authorized person as necessary.
#             </div>

#             <div class="paragraph">
#                 6. The Tenant shall not make any structural modifications to the premises without prior written consent from the House Owner.
#             </div>

#             <div class="paragraph">
#                 7. The Tenant agrees to keep the house premises clean and hygienic, ensuring no damage occurs.
#             </div>

#             <div class="paragraph">
#                 <strong>IN WITNESS WHEREOF</strong>, both parties have signed this agreement on the day, month, and year first mentioned above.
#             </div>

#             <div class="signature">
#                 (<span class="underline">{data.get('landlordName', '________')}</span>)<br>
#                 HOUSE OWNER
#             </div>

#             <div class="witness-section">
#                 <strong>WITNESS:</strong>
#                 <div>1. (<span class="underline">{data.get('witness1', '________')}</span>)</div>
#                 <div>2. (<span class="underline">{data.get('witness2', '________')}</span>)</div>
#             </div>
#         </div>
#     </body>
#     </html>
#     """

def generate_mock_agreement(data):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: "AgentCF", Georgia, serif;
                margin: 10px;
                padding: 10px;
                line-height: 1.5;
                text-align: justify;
                color: #333;
            }}
            .container {{
                width: 100%;
                margin: 0 auto;
                
                padding: 20px;
                border-radius: 8px;
            }}
            p{{
            line-height: 1.2;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
                font-size: 20px;
                margin-bottom: 15px;
                font-weight: bold;
            }}
            .underline {{
                border-bottom: 1px solid #000;
                min-width: 150px;
                display: inline-block;
                margin: 0 5px;
            }}
            .paragraph {{
                margin-bottom: 10px;
            }}
            .signature {{
                margin-top: 20px;
                text-align: right;
                padding-right: 30px;
                font-size:18px;
            }}
            .sign-line {{
                border-top: 1px solid #000;
                display: inline-block;
                width: 180px;
                margin-bottom: 5px;
            }}
            .witness-section {{
                margin-top: 20px;
            }}
            .witness-number{{
               font-size:18px;
               line-height:1.5;
            }}
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                let currentDate = new Date().toLocaleDateString();
                document.getElementById("currentDate").innerText = currentDate;
                document.getElementById("currentTimestamp").innerText = Date.now();
            }});
        </script>
    </head>
    <body>
        <div class="container">
            <h1>RENT AGREEMENT</h1>
            <div class="paragraph">
                This Rent Agreement is executed at <span class="underline">{data.get('state', '________')}</span>, on 
                <p><strong>Date:</strong> <span id="currentDate"></span></p>
            , effective from <span class="underline">{data.get('startDate', '________').split('T')[0] if 'T' in data.get('startDate', '________') else data.get('startDate', '________')}
</span>
                between <span class="underline">{data.get('landlordName', '________')}</span>, R/O
                <span class="underline">{data.get('landlordAddress', '________')}</span>, hereinafter referred to as the "LANDLORD"
                and <span class="underline">{data.get('tenantName', '________')}</span>, residing at <span class="underline">{data.get('tenantAddress', '________')}</span>,
                hereinafter referred to as the "TENANT".
            </div>

            <div class="paragraph">
                WHEREAS the LANDLORD is the lawful owner of the property located at 
                <span class="underline">{data.get('propertyAddress', '________')}</span>, the TENANT has requested to rent 
                the premises for residential purposes, and the LANDLORD agrees to lease the property under the following terms:
            </div>

            <div class="paragraph">
                <strong>1.</strong> The lease shall commence on <span class="underline">{data.get('startDate', '________').split('T')[0] if 'T' in data.get('startDate', '________') else data.get('startDate', '________')}
</span> for a period of
                <span class="underline">{data.get('leaseDuration', '________')}</span> months, wef.
            </div>

            <div class="paragraph">
                <strong>2.</strong>That the rent payable by the Tenant to the House owner or his Authorized person, 
            in respect of the said premises, shall be Rs. <span class="underline">{data.get('monthlyRent', '________')}</span>/- payable
                on or before <span class="underline">{data.get('rentDueDate', '________')}</span> succeeding month in addition to the above mentioned 
            immovable property maintenance charges payable to <span class="underline"></span> Association by the Tenant every month.
            </div>

            <div class="paragraph">
                <strong>3.</strong> The TENANT has paid a refundable security deposit of Rs. <span class="underline">{data.get('securityDeposit', '________')}</span>/-, as interest free rent advance, the receipt of 
            which is hereby acknowledged by the houseowner by these presents.
                This advance 
            amount shall be returned to the tenant by the houseowner at the time of vacating 
            the said premises after adjusting the dues such as rent, water charges, maintenance 
            charges and electricity dues, apart from cost of damages if any.
            </div>

            <div class="paragraph">
            4. That the said house premises have a separate normal three phase household 
            electricity connection and the tenant shall pay the electricity charges to the 
            Electricity Board as per the meter Reading noted in the card.
        </div>

            <div class="paragraph">
                <strong>5.</strong> Either party may terminate the lease by giving a notice of <span class="underline">{data.get('noticePeriod', '________')}</span> months in writing.
                If the TENANT vacates before the lock-in period of <span class="underline">{data.get('lockInPeriod', '________')}</span> months, the security deposit may be forfeited.
            </div>

            <div class="paragraph">
            6. That the Corporation Property tax and water and sewerage tax shall be payable 
            by the house owner but the tenant shall pay the water consumption charges 
            periodically and likewise any running charges consequent to the 
            usage/consumption by the Tenant shall be payable by the tenant.
        </div>

        <div class="paragraph">
            7. That the fittings and fixtures in the house premises are in good condition and the 
            tenant return the same to the house owner in good condition excepting normal 
            wear and tear before vacating the house premises and actual cost of damages if 
            any, shall be reimbursable by the tenant to the house owner.
        </div>

            <div class="paragraph">
                <strong>8. Restrictions:</strong> The premises shall not be sublet, modified, or used for illegal purposes.
            </div>

             <div class="paragraph">
            9. That the tenant has agreed to keep the house premises clean and in hygienic 
            condition including the surrounding areas and the tenant has agreed not to do 
            any action that would cause permanent / structural damages / changes without 
            obtaining prior consent from the owner on impact and costs.
        </div>

        <div class="paragraph">
            10. That the tenant has agreed to hand over main door keys (----Nos), bedroom keys 
            (---Nos), tube lights (---- Nos) and the bulbs with fittings (------- Nos) along with 
            the EB card to the house owner at the time of vacating the house.
        </div>

            <div class="paragraph">
                <strong>11. Jurisdiction:</strong> Any disputes shall be subject to the jurisdiction of <span class="underline">{data.get('state', '________')}</span>.
            </div>

            <div class="paragraph">
            <strong>IN WITNESS WHERE OF</strong>, both the parties have put their hands and signed on the day 
            month and year above written.
        </div>
        <div class="signature">
                    (<span class="underline"></span>)<br>
                    TENANT
                </div>

        <div class="signature">
            (<span class="underline"></span>)<br>
            HOUSE OWNER
        </div>

        <div class="witness-section">
            <strong>WITNESS:-</strong>
            <div class="witness-item">
                <div class="witness-number">1.</div>
                <div></div>

            </div>
            <div class="witness-item">
                <div class="witness-number">2.</div>
                <div></div>
            </div>
        </div>
    </div>
</body>
</html>
    """



# def generate_pdf(text, filename):
#     """ Generate a PDF file with the given text using ReportLab """
#     c = canvas.Canvas(filename, pagesize=letter)
#     c.setFont("Helvetica", 12)

#     y_position = 750  # Initial position
#     line_height = 20  # Spacing between lines

#     for line in text.split("\n"):
#         c.drawString(50, y_position, line)
#         y_position -= line_height
#         if y_position < 50:  # Prevent text from going off the page
#             c.showPage()
#             y_position = 750  # Reset position for new page

#     c.save()

from weasyprint import HTML

def generate_pdf(html_content, filename):
    """ Generate a properly formatted PDF from HTML using WeasyPrint """
    HTML(string=html_content).write_pdf(filename)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# from weasyprint import HTML
# import os

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend-backend communication

# @app.route("/generate-agreement", methods=["POST"])
# def generate_agreement():
#     data = request.json
#     agreement_html = generate_mock_agreement(data)  # Generate agreement as HTML
#     return jsonify({"agreementHtml": agreement_html})

# @app.route("/download-pdf", methods=["POST"])
# def download_pdf():
#     data = request.json
#     agreement_html = data.get("agreementHtml", "")

#     pdf_path = "rental_agreement.pdf"
#     generate_pdf(agreement_html, pdf_path)

#     # Ensure the file exists before sending
#     if not os.path.exists(pdf_path):
#         return jsonify({"error": "Failed to generate PDF"}), 500

#     return send_file(pdf_path, as_attachment=True, mimetype='application/pdf')

# def generate_mock_agreement(data):
#     """ Generate a rental agreement as HTML for WeasyPrint """
    
#     # Fixing list values (in case of array input)
#     payment_methods = ', '.join(data.get('paymentMethods', [])) if isinstance(data.get('paymentMethods'), list) else data.get('paymentMethods', '________')

#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <style>
#             body {{
#                 font-family: Arial, sans-serif;
#                 margin: 20px;
#                 padding: 20px;
#                 line-height: 1.6;
#             }}
#             h1, h2, h3 {{
#                 text-align: center;
#             }}
#             .section {{
#                 margin-bottom: 15px;
#                 border-bottom: 1px solid #ccc;
#                 padding-bottom: 10px;
#             }}
#             .signature {{
#                 margin-top: 30px;
#                 display: flex;
#                 justify-content: space-between;
#             }}
#             .signature div {{
#                 text-align: center;
#                 width: 45%;
#             }}
#         </style>
#     </head>
#     <body>
#         <h1>RENTAL AGREEMENT</h1>
#         <p>This agreement is made at <strong>{data.get('agreementLocation', '________')}</strong> on 
#         <strong>{data.get('agreementDate', '________')}</strong> between:</p>

#         <div class="section">
#             <h2>Landlord Details</h2>
#             <p><strong>Name:</strong> {data.get('landlordName', '________')}</p>
#             <p><strong>Address:</strong> {data.get('landlordAddress', '________')}</p>
#             <p><strong>Phone:</strong> {data.get('landlordPhone', '________')}</p>
#         </div>

#         <div class="section">
#             <h2>Tenant Details</h2>
#             <p><strong>Name:</strong> {data.get('tenantName', '________')}</p>
#             <p><strong>Address:</strong> {data.get('tenantAddress', '________')}</p>
#             <p><strong>Phone:</strong> {data.get('tenantPhone', '________')}</p>
#         </div>

#         <div class="section">
#             <h2>Property Details</h2>
#             <p><strong>Address:</strong> {data.get('propertyAddress', '________')}</p>
#             <p><strong>Property Type:</strong> {data.get('propertyType', '________')}</p>
#         </div>

#         <div class="section">
#             <h2>Rent & Payment</h2>
#             <p><strong>Monthly Rent:</strong> ₹{data.get('rentalAmount', '0')}</p>
#             <p><strong>Due Date:</strong> {data.get('rentDueDate', '________')}</p>
#             <p><strong>Security Deposit:</strong> ₹{data.get('securityDeposit', '0')}</p>
#             <p><strong>Accepted Payment Methods:</strong> {payment_methods}</p>
#         </div>

#         <div class="section">
#             <h2>Termination & Notice</h2>
#             <p><strong>Notice Period:</strong> {data.get('noticePeriod', '0')} months</p>
#             <p><strong>Lock-in Period:</strong> {data.get('lockInPeriod', '0')} months</p>
#         </div>

#         <div class="signature">
#             <div>
#                 <p><strong>House Owner</strong></p>
#                 <p>_________________________</p>
#                 <p>{data.get('landlordName', '________')}</p>
#             </div>
#             <div>
#                 <p><strong>Tenant</strong></p>
#                 <p>_________________________</p>
#                 <p>{data.get('tenantName', '________')}</p>
#             </div>
#         </div>
#     </body>
#     </html>
#     """

# def generate_pdf(html_content, filename):
#     """ Generate a PDF from HTML using WeasyPrint """
#     HTML(string=html_content).write_pdf(filename)
#     print(f"PDF successfully created at {filename}")

# if __name__ == "__main__":
#     app.run(debug=True)