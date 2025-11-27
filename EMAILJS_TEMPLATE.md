# Plantilla EmailJS para La Creativa

Esta es la configuración exacta que debes usar en EmailJS para la plantilla de email.

## Configuración Básica

**Template Name:** `La Creativa - Invoice Template`

## Email Settings

**From Name:**
```
La Creativa
```

**From Email:**
```
{{from_email}}
```
(EmailJS lo configurará automáticamente con tu Gmail)

**To Email:**
```
{{to_email}}
```

**Subject:**
```
Albarà La Creativa - {{client_name}}
```

**Reply To:**
```
hola@lacreativaberga.cat
```

## Email Body (Content)
**Body:**
```html
Hola {{client_name}},

Puedes descargar tu factura número {{invoice_number}} desde este enlace:

{{download_link}}

Total: {{amount}}€

Detalles de los productos:
{{products}}

El enlace de descarga estará disponible permanentemente.

Gracias por confiar en La Creativa.

Saludos,
La Creativa
Carrer del Bruc 1, 08600 Berga, Barcelona
Tel. 693 00 45 22 - 93 194 53 92
hola@lacreativaberga.cat
```

## Variables Dinámicas

Estas variables se envían automáticamente desde `script.js`:

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `{{to_email}}` | Email del cliente | cliente@example.com |
| `{{client_name}}` | Nombre del cliente | Joan García |
| `{{invoice_number}}` | Número de factura | C0033 |
| `{{amount}}` | Total de la factura | 125.50 |
| `{{products}}` | Lista de productos | Producto 1 - 2x 50.00€ = 100.00€ |
| `{{download_link}}` | Link de descarga del PDF | https://xxx.supabase.co/storage/v1/object/public/invoices/... |

**IMPORTANTE:** Ya NO uses la variable `{{pdf_attachment}}` ni configures adjuntos. Ahora se usa un link de descarga.

## Test Template

Una vez configurada la plantilla, puedes probarla con estos valores de ejemplo:

```json
{
  "to_email": "tu-email@example.com",
  "client_name": "Cliente de Prueba",
  "invoice_number": "C0001",
  "amount": "100.00",
  "products": "Producto de prueba - 1x 100.00€ = 100.00€",
  "download_link": "https://xxxxxxxxxxx.supabase.co/storage/v1/object/public/invoices/Factura_C0001_1234567890.pdf"
}
```

## Notas Importantes

1. **No configures adjuntos (attachments)** - Ahora se usa un link de descarga
2. **No cambies los nombres de las variables** (deben coincidir exactamente con lo que envía `script.js`)
3. **El link de descarga es permanente** - El cliente podrá descargar la factura cuando quiera
4. Si quieres recibir una copia de cada email, añade tu email en "BCC" en la configuración de EmailJS

## Personalización Opcional

Si quieres un email más elaborado, puedes usar HTML en el body:

```html
<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
  <h2 style="color: #333;">Hola {{client_name}},</h2>
  
  <p>Adjunto encontrarás el albarà <strong>número {{invoice_number}}</strong> por un importe de <strong>{{amount}}€</strong>.</p>
  
  <h3>Detalles de los productos:</h3>
  <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">{{products}}</pre>
  
  <p>Gracias por confiar en La Creativa.</p>
  
  <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
  
  <p style="color: #666; font-size: 12px;">
    <strong>La Creativa</strong><br>
    Carrer del Bruc 1, 08600 Berga, Barcelona<br>
    Tel. 693 00 45 22 - 93 194 53 92<br>
    <a href="mailto:hola@lacreativaberga.cat">hola@lacreativaberga.cat</a>
  </p>
</div>
```
