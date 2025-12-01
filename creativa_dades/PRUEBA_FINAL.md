# 🧪 PRUEBA FINAL DEL SISTEMA COMPLETO

¡Todo está configurado! Es hora de verificar que todo funciona perfectamente.

## 1. Generar Factura de Prueba

1. Abre `index.html` en tu navegador.
2. Rellena el formulario con datos de prueba:
   - **Cliente:** Prueba Final
   - **Email:** TU EMAIL (para recibir el correo)
   - **Producto:** Test, Precio: 10, Cantidad: 1
3. Click en **"Generar i Enviar Factura"**.

## 2. Verificar Resultados

Deberías ver en pantalla:
- ✅ "Generant factura..."
- ✅ "Pujant PDF a Supabase..."
- ✅ "Enviant correu..."
- ✅ "Guardant dades a Supabase..."
- ✅ **"✓ Factura generada, guardada i enviada correctament"**

## 3. Verificar en Supabase (Opcional)

Si quieres estar 100% seguro, ve a tu Dashboard:
- **Storage → invoices:** Deberías ver el PDF nuevo.
- **Table Editor → invoices:** Deberías ver la nueva fila con los datos.
- **Table Editor → clients:** Deberías ver el cliente "Prueba Final".

## 4. Verificar Email

- Revisa tu bandeja de entrada.
- Abre el email.
- Click en el enlace de descarga → **El PDF debe descargarse.**

---

**¡Haz la prueba ahora!** Si todo sale bien, ¡hemos terminado! 🎉
