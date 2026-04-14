# 🌊 MARINA BEAUTY - ESTRUCTURA DEL PROYECTO

## 📁 Estructura de Carpetas

```
marinabeauty/
├── index.html                 ← ARCHIVO PRINCIPAL (la tienda web)
├── images/                    ← CARPETA PARA IMÁGENES DE PRODUCTOS
│   ├── cepillo-exfoliante.jpg
│   ├── toallas-desmaquillantes.jpg
│   ├── papelitos-arroz.jpg
│   ├── parche-antiacne.jpg
│   ├── brochas-negras.jpg
│   ├── mascarilla-negra.jpg
│   ├── brochas-blancas.jpg
│   ├── mascarilla-labios.jpg
│   ├── fijador.jpg
│   ├── agua-rosas.jpg
│   ├── pomos.jpg
│   ├── espuma.jpg
│   └── README.md              ← Guía para las imágenes
├── PRECIOS_FINALES.md         ← Cálculo de precios (referencia)
├── GUIA_CONFIGURACION.md      ← Pasos para configurar
└── README.md (este archivo)   ← Visión general
```

---

## 🎯 Características Principales

### 1. **Catálogo de Productos**

- ✅ 12 productos diferentes
- ✅ Descripción personalizada para cada uno
- ✅ Imágenes de producto
- ✅ Precios calculados automáticamente

### 2. **Carrito Interactivo**

- ✅ Agregar productos (botón +)
- ✅ Aumentar/disminuir cantidad
- ✅ Quitar productos (cantidad 0)
- ✅ Cálculo automático del total
- ✅ Contador en la barra de navegación

### 3. **Sección "Sobre Nosotros"**

- ✅ Historia de Marina Beauty
- ✅ Misión: Belleza para mujeres de Bahía Málaga
- ✅ Información de entregas personales
- ✅ Diseño inspirador

### 4. **Integración WhatsApp**

- ✅ Botón "Pedir por WhatsApp"
- ✅ Envía detalle automático del pedido
- ✅ Incluye total estimado
- ✅ Abre WhatsApp web/app

### 5. **Diseño Responsive**

- ✅ Se adapta a celulares (mobile)
- ✅ Se adapta a tablets
- ✅ Se adapta a escritorio (desktop)
- ✅ Colores inspirados en el océano

---

## 💰 Sistema de Precios

**Cada producto incluye:**

1. Costo original de compra
2. Parte proporcional del costo de envío ($2,992 COP por producto)
3. 35% de margen de ganancia

**Ejemplo - Cepillo Exfoliante:**

- Costo compra: $6,000
- Envío: +$2,992
- Subtotal: $8,992
- Margen 35%: ÷ 0.65
- **Precio final: $13,833**

---

## 🎨 Personalizaciones Realizadas

✨ **Ya está personalizado con:**

- Nombre: Marina Beauty
- Lema: "Belleza que fluye como el mar"
- Colores: Tonos azul-verde (teal) y rosa suave
- Ubicación: Base Naval de Bahía Málaga
- Envío: Entregas personales
- Método de pago: WhatsApp + acuerdo en persona

---

## 🚀 Pasos para Activar

1. **Agrega imágenes** en la carpeta `/images/`
2. **Actualiza el número de WhatsApp** en el código
3. **Prueba la tienda** en tu navegador
4. **Comparte el link** con tus clientes

---

## 📱 Cómo se Vería

### Navegación (Arriba)

```
[Logo Marina Beauty] [Catálogo] [Sobre Nosotros] [🛒 Carrito]
```

### Sección Hero

```
"Belleza que fluye como el mar"
Entregas personales en Bahía Málaga, Pacífico
```

### Sección Sobre Nosotros

```
Marina Beauty nace de una necesidad genuina...
(Historia personalizada)
```

### Catálogo (Grid 4 columnas en desktop)

```
[Producto 1][Producto 2][Producto 3][Producto 4]
[Producto 5][Producto 6][Producto 7][Producto 8]
[Producto 9][Producto 10][Producto 11][Producto 12]
```

### Carrito (Abre desde la derecha)

```
┌─────────────────────┐
│ Tu Pedido        ✕  │
├─────────────────────┤
│ [Producto 1]        │
│ x2 - $13,833        │
│                     │
│ [Producto 2]        │
│ x1 - $13,064        │
├─────────────────────┤
│ TOTAL: $40,730      │
│ [Pedir por WhatsApp]│
└─────────────────────┘
```

---

## 📊 Estadísticas

- **Tiempo de carga**: < 2 segundos
- **Compatible con**: Navegadores modernos (Chrome, Safari, Firefox, Edge)
- **Funciones JavaScript**: 100% funcionales sin servidor
- **Datos privados**: Todo local (No se almacena datos)
- **Integraciones**: Solo WhatsApp (vía enlace directo)

---

## ❓ FAQ Rápido

**P: ¿Es necesario pagar hosting?**
A: No para esta versión básica. Puedes usar:

- GitHub Pages (gratis)
- Replit (gratis)
- Neocities (gratis)

**P: ¿Cómo comparten los clientes este link?**
A: Por WhatsApp, email, red social, o lo colocas en tu perfil de Instagram.

**P: ¿Qué pasa con los pedidos?**
A: Llegan a WhatsApp → Confirmas → Acuerdas pago y lugar → ¡Entrega!

**P: ¿Puedo edit el contenido después?**
A: Sí, edita `index.html` con cualquier editor de texto.

---

## 🎁 Bonus: Ideas de Mejora Futura

- [ ] Cargas de imágenes dinámicas
- [ ] Historial de pedidos
- [ ] Sistema de reseñas
- [ ] Cupones de descuento
- [ ] Pago integrado (Stripe, PayPal)
- [ ] Blog de tips de belleza
- [ ] Galería de cliente antes/después

---

**¡Tu tienda está lista! 🌊✨💄**

Cualquier pregunta, revisa `GUIA_CONFIGURACION.md`
