PHONE_REGEX = r'^\+?1?\d{9,15}$'

PHONE_MESSAGE = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."

INVOICE_HTML = """<html>
  <head>
    <meta charset="utf-8">
    <link href="invoice.css" media="print" rel="stylesheet">
    <title>Invoice</title>
    <meta name="description" content="Invoice demo sample">
  </head>

  <body>
    <h1>Invoice</h1>

    <aside>
      <address id="from">
        WeasyPrint
        26 rue Emile Decorps
        69100 Villeurbanne
        France
      </address>

      <address id="to">
        Our awesome developers
        From all around the world
        Earth
      </address>
    </aside>

    <dl id="informations">
      <dt>Invoice number</dt>
      <dd>12345</dd>
      <dt>Date</dt>
      <dd>March 31, 2018</dd>
    </dl>

    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Subtotal</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Website design</td>
          <td>€34.20</td>
          <td>100</td>
          <td>€3,420.00</td>
        </tr>
        <tr>
          <td>Website development</td>
          <td>€45.50</td>
          <td>100</td>
          <td>€4,550.00</td>
        </tr>
        <tr>
          <td>Website integration</td>
          <td>€25.75</td>
          <td>100</td>
          <td>€2,575.00</td>
        </tr>
      </tbody>
    </table>

    <table id="total">
      <thead>
        <tr>
          <th>Due by</th>
          <th>Account number</th>
          <th>Total due</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>May 10, 2018</td>
          <td>132 456 789 012</td>
          <td>€10,545.00</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>"""