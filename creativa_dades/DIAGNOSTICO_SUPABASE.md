# 🔍 Diagnóstico: Datos no se guardan en Supabase

## Paso 1: Ver Errores en la Consola

1. Abre `index.html` en tu navegador
2. Presiona **F12** (o Click derecho → Inspeccionar)
3. Ve a la pestaña **"Console"**
4. Genera una factura
5. **Busca mensajes en rojo** relacionados con Supabase

## Errores Comunes

### Error 1: "relation 'public.invoices' does not exist"
**Solución:** Las tablas no se crearon correctamente. Vuelve a ejecutar el SQL.

### Error 2: "column 'xxx' does not exist"
**Solución:** Hay un desajuste entre los nombres de columnas. Verifica que ejecutaste el SQL correcto.

### Error 3: "Invalid API key"
**Solución:** La anon key está mal configurada en script.js.

### Error 4: Sin errores pero no se guarda
**Solución:** Verifica que las funciones se están llamando correctamente.

## Paso 2: Verificación Rápida

Abre la consola del navegador y ejecuta esto para probar la conexión:

```javascript
// Test de conexión a Supabase
(async () => {
  const testData = {
    invoice_id: 'TEST001',
    document_type: 'Comanda',
    date: new Date().toISOString(),
    client_name: 'Test Client',
    total_general: 100
  };
  
  const { data, error } = await supabaseClient
    .from('invoices')
    .insert([testData]);
  
  console.log('Test result:', { data, error });
})();
```

**Si ves un error, cópiamelo aquí.**

## Paso 3: Verificar Nombres de Tablas

En Supabase Dashboard → **Table Editor**, verifica que las tablas se llaman exactamente:
- `invoices` (minúsculas, plural)
- `clients` (minúsculas, plural)

## Paso 4: Verificar que RLS está Desactivado

En **Table Editor** → Click en cada tabla → Debería decir **"RLS disabled"** o **"Unrestricted"**.

Si dice **"RLS enabled"**, ejecuta esto en SQL Editor:

```sql
ALTER TABLE clients DISABLE ROW LEVEL SECURITY;
ALTER TABLE invoices DISABLE ROW LEVEL SECURITY;
```

---

**¿Qué errores ves en la consola (F12) cuando generas una factura?**
