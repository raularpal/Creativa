-- Ejecuta este código en el SQL Editor de tu proyecto en Supabase
-- para añadir las columnas necesarias para el descuento y las observaciones.

ALTER TABLE invoices ADD COLUMN discount numeric DEFAULT 0;
ALTER TABLE invoices ADD COLUMN observations text;
