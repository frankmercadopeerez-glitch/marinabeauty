# 🎨 GUÍA DE CONFIGURACIÓN - MARINA BEAUTY

## ✅ Lo que ya está listo:

1. **Catálogo Completo** - 12 productos con descripciones
2. **Precios Calculados** - Con margen 35% + envío distribuido
3. **Carrito Funcional** - Agregar/quitar productos
4. **Sección "Sobre Nosotros"** - Historia de Marina Beauty
5. **Botón WhatsApp** - Integración directa para pedidos
6. **Diseño Responsive** - Se ve bien en mobile, tablet y desktop

---

## 📸 Próximo Paso: Cargar las Imágenes

### Instrucciones:

1. **Crea estos archivos en la carpeta `/images/`:**
   - Puedes capturar pantallas de las imágenes adjuntas que recibiste
   - O tomar fotos de los productos reales
   - O descargar imágenes similares de internet

2. **Nombra los archivos exactamente así:**

   ```
   cepillo-exfoliante.jpg
   toallas-desmaquillantes.jpg
   papelitos-arroz.jpg
   parche-antiacne.jpg
   brochas-negras.jpg
   mascarilla-negra.jpg
   brochas-blancas.jpg
   mascarilla-labios.jpg
   fijador.jpg
   agua-rosas.jpg
   pomos.jpg
   espuma.jpg
   ```

3. **Formato recomendado:**
   - JPG o PNG
   - Tamaño: 400x400 píxeles (cuadrado)
   - Peso: 100-200 KB máximo

### ⚠️ Si las imágenes no se muestran:

- Verifica que estén en la carpeta `/images/`
- Asegúrate que el nombre sea exacto (sin espacios, lowercase)
- Recarga la página con F5
- Abre la consola (F12) para ver errores

---

## 📱 Configurar el Número de WhatsApp

En el archivo `index.html`, busca esta línea:

```javascript
const NUMERO_WHATSAPP = "573000000000";
```

**Cambia por tu número real:**

- Incluye código de país: **57** (Colombia)
- Sin espacios ni caracteres especiales
- Ejemplo: `573015041234`

---

## 💡 Personalizaciones Opcionales

### Cambiar el nombre de la tienda:

- Búsca: `<title>Marina Beauty | Belleza que fluye como el mar</title>`
- Puedes editar "Marina Beauty" por otro nombre

### Cambiar colores:

- Los colores están en la sección `tailwind.config`
- `marina-teal`: #1f8f9f (azul-verde principal)
- `marina-pink`: #f79fb0 (rosa suave)
- `marina-light`: #e0f6f9 (fondo celeste)

### Cambiar descripciones:

- Busca cada producto en el array `productos`
- Edita la propiedad `description`

---

## 🚀 Publicar la Página

### Opción 1: Replit (Gratis y fácil)

1. Copia el contenido de `index.html`
2. Crea una cuenta en replit.com
3. Sube los archivos
4. Comparte el link público

### Opción 2: GitHub Pages (Gratis)

1. Crea un repositorio en github.com
2. Sube tus archivos
3. Ve a Settings → Pages → Branch: main
4. Tu web estará en: `tuusuario.github.io/marinabeauty`

### Opción 3: Tu propio servidor/hosting

1. Sube los archivos vía FTP
2. Accede por tu dominio

---

## 📊 Monitoreo de Ventas

Cuando recibas pedidos por WhatsApp:

1. El cliente verá el total estimado en el mensaje
2. Tú confirmas el monto final
3. Acuerdas método de pago y lugar de entrega
4. ¡A empacar y entregar! 📦

---

## 🎯 Checklist Final:

- [ ] Imágenes subidas en `/images/`
- [ ] Número de WhatsApp actualizado
- [ ] Descripciones personalizadas (opcional)
- [ ] Página probada desde celular
- [ ] Probado agregar/quitar del carrito
- [ ] Probado el botón "Pedir por WhatsApp"
- [ ] Link listo para compartir con clientes

---

## ❓ Preguntas Frecuentes

**P: ¿Los clientes pueden pagar online?**
A: No en esta versión básica. Los pagos se acuerdan por WhatsApp y se hacen en persona.

**P: ¿Puedo cambiar los precios?**
A: Sí, edita el `basePrice` de cada producto. El sistema recalcula automáticamente.

**P: ¿Cómo actualizo la cantidad de envío?**
A: Cambia `COSTO_ENVIO_TOTAL` en el script JavaScript.

**P: ¿Puedo agregar más productos?**
A: Sí, agrega un nuevo objeto al array `productos` y crea su imagen correspondiente.

---

**¡Estás lista para emezar! 🌊✨**
