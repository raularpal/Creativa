# 🔄 Configuración Supabase desde CERO

## Paso 1: Limpiar TODO (2 min)

Ve a **Supabase Dashboard → SQL Editor** y ejecuta esto para eliminar todo:

```sql
-- Eliminar todas las tablas existentes
DROP TABLE IF EXISTS invoices CASCADE;
DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS comandes CASCADE;
```

Click **"Run"**.

---

## Paso 2: Crear Tablas NUEVAS (2 min)

En el mismo **SQL Editor**, ejecuta esto:

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

-- Desactivar RLS (seguridad)
ALTER TABLE clients DISABLE ROW LEVEL SECURITY;
ALTER TABLE invoices DISABLE ROW LEVEL SECURITY;
```

Click **"Run"**.

---

## Paso 3: Verificar que se crearon (1 min)

1. Ve a **Table Editor**
2. Deberías ver **2 tablas**:
   - `clients`
   - `invoices`
3. Click en `invoices` → Deberías ver **22 columnas**

---

## Paso 4: Probar inserción (1 min)

En la **consola del navegador** (F12 → Console), ejecuta:

```javascript
(async () => {
  const test = {
    invoice_id: 'TEST001',
    document_type: 'Comanda',
    client_name: 'Cliente Test',
    total_general: 99.99
  };
  
  const { data, error } = await supabaseClient
    .from('invoices')
    .insert([test])
    .select();
  
  console.log(error ? '❌ Error:' : '✅ Éxito:', error || data);
})();
```

**Si ves "✅ Éxito"**, las tablas están bien configuradas.

---

## Paso 5: Probar la aplicación (1 min)

1. Genera una factura desde `index.html`
2. Deberías ver:
   - ✅ PDF descargado
   - ✅ PDF subido a Storage
   - ✅ Email enviado
   - ✅ **Datos guardados en Supabase**

3. Verifica en **Table Editor → invoices** → Deberías ver la factura

---

## 🆘 Si sigue sin funcionar

Copia el **error exacto** de la consola y dímelo.

---

**Ejecuta los pasos 1 y 2 ahora (el SQL) y dime si ves las tablas en Table Editor.**
