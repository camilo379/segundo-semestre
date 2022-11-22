class Tienda:
  def __init__(self):
 
   self.pedido = ([])
   self.producto = ([])
   self.contraseña = ([])
  def infouser(self):
    contraseña= int(input("dijite su contraseña"))
    if contraseña ==(1103):
      self.contraseña.append(1103)
    else:
      self.infouser()

    print("1 = camisa")
    print("2 = pantalon")
    print("3 = tenis")
    elejido= int(input("dijite su prenda"))
    if elejido == 1:
      self.producto.append("camisa")
      self.pedido.append(35000)
    if elejido == 2:
      self.producto.append("pantalon")
      self.pedido.append(50000)
    if elejido == 3:
       self.producto.append("tenis")
       self.pedido.append(150000)
    if elejido > 3 :
      
        self.infouser()
    print("efectivo")
    print("tarjeta")
    print("nequi")
    self.pago = input("que modo de pago desea aplicar")
    if self.pago=="efectivo" or self.pago=="nequi" or self.pago=="tarjeta":
      self.GenerarFactura()
    else:
      self.infouser()
  def GenerarFactura(self):
    import datetime
    import qrcode
    
    from reportlab.pdfgen import canvas
    totalsuma = sum(self.pedido)
    totaliva= totalsuma * 0.19
    totalApagar= totalsuma + totaliva

    img = qrcode.make("gracias por tu compra te esperamos pronto nuevamente en JCA")
    f = open("codigoqr.png","wb")
    img.save(f)
    print("tienda JCA")
    print("====================")
    print("ciudad de neiva")
    print("tel. 3158178155")
    print("servicioalclientetiendaJCA.com.co")
    Fecha = datetime.datetime.now()
    fecha= datetime.datetime.strftime(Fecha, "%d/%m/%Y")
    hora= datetime.datetime.strftime(Fecha, "%H:%M:%S")
    print("Fecha : ",fecha," Hora : ",hora)
    print("====================")
    print("productos a pagar")
    print("modo de pago=",self.pago)
    print("Producto = "+f"{self.pedido}")
    print("IVA="f"{totaliva}")
    print("total a pagar ="+f"{totalsuma}")
    print("====================")
    print("Visita nuestra pagina web")
    print("Escaneando el siguiente QR")
    print("===================")
    print("Si requiere Factura electronica de venta")
    print("Solicitela en el siguiente correo:")
    print("solicitefacturadecompra@tiendaJCA.com.co")

    pdf = canvas.Canvas("Factura.pdf")
    pdf.drawString(250, 800,"tienda JCA")
    pdf.drawString(200, 780, "====================")
    pdf.drawString(200, 760, "ciudad de neiva")
    pdf.drawString(200, 740, "tel. 3158178155")
    pdf.drawString(200, 720, "servicioalclientetiendaJCA.com.co")
    pdf.drawString(200, 700, "==============================")
    pdf.drawString(200, 680, "fecha: "+f"{fecha} hora: "+f"{hora}")
    pdf.drawString(200, 660, "==============================")
    pdf.drawString(200, 640, "modo de pago = "f"{self.pago}")
    pdf.drawString(200,620,  "productos a pagar:")
    pdf.drawString(200, 600, "producto                 "+f"{self.producto}")
    pdf.drawString(200, 580,"precio                       "+f"{totalsuma}")
    pdf.drawString(200,560, "iva                            "+f"{totaliva}")
    pdf.drawString(200, 540, "totalApagar               "+f"{totalApagar}")
    pdf.drawString(200, 520, "==============================")
    pdf.drawString(200, 500, "Visita nuestra pagina web")
    pdf.drawString(200, 480, "Escaneando el siguiente QR")
    pdf.drawString(200, 460, "==============================")
    pdf.drawImage("codigoqr.png", 250,350, width=110, height=110)
    pdf.drawString(200, 330, "==============================")
    pdf.drawString(200, 310, "Si requiere Factura electronica de venta")
    pdf.drawString(200, 290, "solicitela en el siguiente correo:")
    pdf.drawString(200, 270, "solicitefacturadecompra@tiendaJCA.com.co")
    pdf.save()
    
camilo = Tienda()
camilo.infouser()