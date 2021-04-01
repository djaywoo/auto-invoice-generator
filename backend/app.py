import io
import os
from datetime import datetime

from flask import Flask, render_template, request, send_file, send_from_directory
from weasyprint import HTML

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    posted_data = request.get_json() or {}
    today = datetime.today().strftime("%B %d, %Y")
    default_data = {
        'duedate': 'August 1, 2020',
        'from_addr': {
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345',
            'company_name': 'Python Tip'
        },
        'invoice_number': 123,
        'items': [
            {
                'index': 0,
                'hsn': 3924,
                'qty': 234,
                'rate': 180.0,
                'title': 'website design'
            },
            {
                'index': 1,
                'hsn': 3924,
                'qty': 24,
                'rate': 180.0,
                'title': 'Water jug'
            },
        ],
        'to_addr': {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }
    }

    senderGst = posted_data.get('sender_gst')
    senderMobile = posted_data.get('sender_mobile')
    transport = posted_data.get('transport_details')
    amountInWords = posted_data.get('amountInWords')

    discount = posted_data.get('discount')
    extraCost = posted_data.get('extraCost')
    totalBeforeTax = posted_data.get('totalBeforeTax')
    cgst = posted_data.get('cgst')
    cgstAmount = posted_data.get('cgstAmount')
    sgst = posted_data.get('sgst')
    sgstAmount = posted_data.get('sgstAmount')
    igst = posted_data.get('igst')
    igstAmount = posted_data.get('igstAmount')
    netAmount = posted_data.get('netAmount')

    duedate = posted_data.get('duedate', default_data['duedate'])
    from_addr = posted_data.get('from_addr', default_data['from_addr'])
    to_addr = posted_data.get('to_addr', default_data['to_addr'])
    invoice_number = posted_data.get('invoice_number',
                                     default_data['invoice_number'])
    items = posted_data.get('items', default_data['items'])

    rendered = render_template('invoice.html',
                               date=today,
                               from_addr=from_addr,
                               to_addr=to_addr,
                               items=items,
                               invoice_number=invoice_number,
                               duedate=duedate,
                               senderGst=senderGst,
                               senderMobile=senderMobile,
                               transport_details=transport,
                               amountInWords=amountInWords,
                               discount=discount,
                               extraCost=extraCost,
                               totalBeforeTax=totalBeforeTax,
                               cgst=cgst,
                               cgstAmount=cgstAmount,
                               sgst=sgst,
                               sgstAmount=sgstAmount,
                               igst=igst,
                               igstAmount=igstAmount,
                               netAmount=netAmount
                               )
    # return rendered
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()
    generated_pdf = send_file(
        io.BytesIO(rendered_pdf),
        attachment_filename='invoice.pdf'
    )

    # return 'hello'
    return generated_pdf
    # print(generated_pdf)
    # with open("invoice.pdf", "wb") as f:


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
