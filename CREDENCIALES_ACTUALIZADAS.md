# ✅ Credenciales Actualizadas

He actualizado `script.js` con las credenciales de tu **nuevo proyecto de Supabase**:

- **Project URL:** https://vglkqvfseqxjvivcahcp.supabase.co
- **Anon Key:** Configurada ✅

---

## 🎯 Próximos Pasos

### 1️⃣ ¿Ya creaste el bucket `invoices`? (Paso 2)
Si no, ve a **Storage** → Create bucket:
- Name: `invoices`
- Public: ✅ Marcado
- Configurar 2 políticas (INSERT y SELECT)

### 2️⃣ ¿Ya ejecutaste el SQL para crear las tablas? (Paso 3)
Si no, ve a **SQL Editor** y ejecuta el SQL del archivo SETUP_SUPABASE_NUEVO.md

### 3️⃣ Probar el sistema completo

Una vez que hayas hecho los pasos 1 y 2:

1. Abre `index.html` en tu navegador
2. Genera una factura de prueba
3. Deberías ver:
   - ✅ PDF descargado
   - ✅ "Pujant PDF a Supabase..."
   - ✅ "Enviant correu..."
   - ✅ "Guardant dades a Supabase..."
   - ✅ **"✓ Factura generada, guardada i enviada correctament"**

4. Verifica en Supabase:
   - **Storage → invoices** → PDF subido
   - **Table Editor → invoices** → Factura guardada
   - **Table Editor → clients** → Cliente guardado

5. Verifica email:
   - Revisa bandeja de entrada
   - Click en link → Descarga PDF

---

## 📋 Checklist

- [x] Credenciales actualizadas en script.js
- [ ] Bucket `invoices` creado (público)
- [ ] Políticas del bucket configuradas
- [ ] Tablas creadas (SQL ejecutado)
- [ ] Prueba completa realizada

---

**Dime cuando hayas completado los pasos 2 y 3 (bucket y tablas) y probamos el sistema.**
