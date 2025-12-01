# 🚀 Configuración Supabase - Proyecto Nuevo

## 📋 Paso 1: Obtener Credenciales (2 min)

1. En tu **nuevo proyecto de Supabase**, ve a **Settings** (⚙️ en el menú lateral)
2. Click en **API**
3. Copia estos 2 valores:

### Project URL
Busca "Project URL" y copia el valor (ejemplo: `https://xxxxxxxxxxx.supabase.co`)

### anon/public key
Busca "Project API keys" → **anon** **public** y copia la clave larga (empieza con `eyJhbGci...`)

**📝 Guarda estos 2 valores, los necesitarás en el Paso 4.**

---

## 📋 Paso 2: Crear Bucket de Storage (2 min)

1. En el menú lateral → **Storage**
2. Click **"Create a new bucket"**
3. Configuración:
   - **Name:** `invoices`
   - **Public bucket:** ✅ **MARCAR** (importante)
4. Click **"Create bucket"**

### Configurar Políticas del Bucket

1. Click en el bucket `invoices` que acabas de crear
2. Ve a la pestaña **"Policies"**
3. Click **"New Policy"** → **"For full customization"**

**Política 1 - Permitir subidas:**
```sql
CREATE POLICY "Allow public uploads"
ON storage.objects
FOR INSERT
TO public
WITH CHECK (bucket_id = 'invoices');
```
Click **"Review"** → **"Save policy"**

**Política 2 - Permitir descargas:**
```sql
CREATE POLICY "Allow public downloads"
ON storage.objects
FOR SELECT
TO public
USING (bucket_id = 'invoices');
```
Click **"Review"** → **"Save policy"**

---

## 📋 Paso 3: Crear Tablas (2 min)

1. En el menú lateral → **SQL Editor**
2. Click **"New query"**
3. Copia y pega este SQL:

```sql
-- Tabla de Clientes
CREATE TABLE clients (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    name TEXT NOT NULL,
    nif TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    last_purchase TIMESTAMPTZ
);

-- Tabla de Facturas
CREATE TABLE invoices (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    invoice_id TEXT UNIQUE NOT NULL,
    document_type TEXT,
    date TIMESTAMPTZ,
    entry_date TEXT,
    delivery_date TEXT,
    client_name TEXT,
    client_nif TEXT,
    client_phone TEXT,
    client_email TEXT,
    client_address TEXT,
    client_city TEXT,
    client_zip TEXT,
    items JSONB,
    subtotal NUMERIC(10,2),
    iva_applied BOOLEAN,
    iva_total NUMERIC(10,2),
    total_general NUMERIC(10,2),
    payment_method TEXT,
    paid_status TEXT,
    pdf_url TEXT
);

-- Desactivar RLS
ALTER TABLE clients DISABLE ROW LEVEL SECURITY;
ALTER TABLE invoices DISABLE ROW LEVEL SECURITY;
```

4. Click **"Run"** (o Ctrl+Enter / Cmd+Enter)

### Verificar

Ve a **Table Editor** → Deberías ver 2 tablas:
- `clients`
- `invoices`

---

## 📋 Paso 4: Dame las Credenciales

**Necesito que me des:**

1. **Project URL** (del Paso 1)
2. **anon/public key** (del Paso 1)

Con esos 2 valores, actualizaré `script.js` automáticamente.

---

## ✅ Checklist

- [ ] Paso 1: Copiar Project URL y anon key
- [ ] Paso 2: Crear bucket `invoices` (público)
- [ ] Paso 2: Configurar 2 políticas del bucket
- [ ] Paso 3: Ejecutar SQL para crear tablas
- [ ] Paso 3: Verificar tablas en Table Editor
- [ ] Paso 4: Darme las 2 credenciales

---

**Cuando completes los pasos 1-3, dame las credenciales y lo configuro todo.**
