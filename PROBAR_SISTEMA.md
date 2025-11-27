# ✅ ¡CONFIGURACIÓN COMPLETA!

Todas las credenciales están configuradas en `script.js`:

## EmailJS ✅
- **Public Key:** TGdKTFye8bJ5CTA8X
- **Service ID:** service_qph3d3n
- **Template ID:** template_jrkiu39

## Supabase ✅
- **Project URL:** https://tpnycyjwqnfqqpwukplb.supabase.co
- **Anon Key:** Configurada

---

# 🧪 PRUEBA EL SISTEMA AHORA

## Paso 1: Abrir la aplicación
1. Ve a la carpeta: `/Users/arpal/.gemini/antigravity/scratch/creativa_dades/`
2. Haz doble click en **`index.html`** (se abrirá en tu navegador)

## Paso 2: Generar factura de prueba
Rellena el formulario con estos datos de prueba:

**Cliente:**
- Tipo de documento: Comanda
- Cliente: Test Prueba
- NIF/DNI: 12345678A
- Teléfono: 600000000
- **Email:** **TU EMAIL PERSONAL** ← IMPORTANTE (para recibir el email)

**Producto 1:**
- Nombre: Producto de Prueba
- Precio unitario: 10.00
- Cantidad: 1

**Opcional:**
- Método de pago: Efectiu
- Pagado: Sí
- Aplicar IVA: ☑️ (marcado)

## Paso 3: Click en "Generar i Enviar Factura"

**Deberías ver en pantalla (en este orden):**
1. ✅ "Generant factura..."
2. ✅ PDF se descarga automáticamente (Factura_C0001.pdf)
3. ✅ "Pujant PDF a Supabase..."
4. ✅ "Enviant correu..."
5. ✅ "✓ Factura generada i enviada correctament"

## Paso 4: Verificar el email
1. Revisa tu **bandeja de entrada** (y carpeta spam)
2. Deberías recibir un email con asunto: **"Albarà La Creativa - Test Prueba"**
3. El email debe contener un **link de descarga**
4. Click en el link → Debe descargar el PDF

## Paso 5: Verificar Supabase (opcional)
1. Ve a https://app.supabase.com
2. Tu proyecto → Storage → invoices
3. Deberías ver el PDF subido (Factura_C0001_xxxxxxxxx.pdf)

---

## 🆘 Si algo falla

### Abre la consola del navegador (F12)
- Pestaña "Console"
- Busca mensajes en rojo (errores)
- Copia el error y dímelo

### Problemas comunes:

**"Error pujant PDF"**
- Verifica que el bucket `invoices` existe en Supabase
- Verifica que tiene las 2 políticas configuradas

**"Error enviant correu"**
- Verifica las credenciales de EmailJS
- Verifica que la plantilla existe

**El link del email no funciona**
- Verifica que el bucket es público
- Verifica la política de SELECT

---

## ✅ Si todo funciona

¡Felicidades! Tu sistema de facturas está completo y funcionando:
- ✅ Genera PDFs profesionales
- ✅ Los descarga automáticamente
- ✅ Los sube a Supabase (almacenamiento en la nube)
- ✅ Envía emails a los clientes con link de descarga
- ✅ Los clientes pueden descargar sus facturas cuando quieran

---

**¡PRUEBA AHORA!** Abre `index.html` y genera tu primera factura 🎉
