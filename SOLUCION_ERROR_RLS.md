# 🔧 SOLUCIÓN AL ERROR - Configurar Políticas Supabase

## El Error
```
Error: new row violates row-level security policy
```

**Causa:** El bucket `invoices` existe pero no tiene las **políticas de acceso público** configuradas.

---

## ✅ SOLUCIÓN (5 minutos)

### Paso 1: Ir a Supabase Storage
1. Ve a https://app.supabase.com
2. Selecciona tu proyecto
3. Menú lateral → **Storage**
4. Click en el bucket **`invoices`**

### Paso 2: Configurar Políticas
1. En el bucket `invoices`, busca la pestaña **"Policies"** (arriba)
2. Click en **"New Policy"**
3. Selecciona **"For full customization"** (o "Get started quickly" → "Public access")

### Paso 3: Crear Política de INSERT (Permitir subidas)

Si elegiste "For full customization":

**Nombre de la política:** `Allow public uploads`

**SQL de la política:**
```sql
CREATE POLICY "Allow public uploads"
ON storage.objects
FOR INSERT
TO public
WITH CHECK (bucket_id = 'invoices');
```

Click **"Review"** → **"Save policy"**

### Paso 4: Crear Política de SELECT (Permitir descargas)

Click de nuevo en **"New Policy"** → **"For full customization"**

**Nombre de la política:** `Allow public downloads`

**SQL de la política:**
```sql
CREATE POLICY "Allow public downloads"
ON storage.objects
FOR SELECT
TO public
USING (bucket_id = 'invoices');
```

Click **"Review"** → **"Save policy"**

---

## 🎯 ALTERNATIVA MÁS RÁPIDA

Si Supabase te ofrece opciones predefinidas:

1. En "New Policy" → Click **"Get started quickly"**
2. Selecciona **"Public access"** o **"Enable public access"**
3. Marca ambas opciones:
   - ✅ Allow uploads
   - ✅ Allow downloads
4. Click **"Save"**

---

## ✅ Verificar que Funcionó

Después de configurar las políticas:

1. En el bucket `invoices` → Pestaña **"Policies"**
2. Deberías ver **2 políticas activas**:
   - Una para INSERT (subidas)
   - Una para SELECT (descargas)

---

## 🧪 Probar de Nuevo

1. Vuelve a `index.html` en tu navegador
2. Genera otra factura (puedes usar los mismos datos)
3. Ahora DEBERÍA funcionar:
   - ✅ PDF se descarga
   - ✅ Se sube a Supabase (verás el archivo en Storage)
   - ✅ Se envía el email

---

## 🆘 Si sigue sin funcionar

Verifica que:
- ✅ El bucket se llama exactamente `invoices` (sin espacios, minúsculas)
- ✅ El bucket es **público** (checkbox marcado al crearlo)
- ✅ Tienes 2 políticas activas (INSERT y SELECT)

---

**Configura las políticas ahora y prueba de nuevo. ¡Debería funcionar inmediatamente!**
