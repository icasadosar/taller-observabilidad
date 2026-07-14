# Taller de Observabilidad

Este repositorio contiene el entorno de prácticas y laboratorios para el **Taller de Observabilidad de 3 Sesiones**. A lo largo de este taller, aprenderás a instrumentar aplicaciones y configurar la pila de observabilidad estándar de la industria usando **FastAPI, Prometheus, Loki, Promtail, cAdvisor y Grafana**.

---

## 🗺️ Arquitectura del Entorno

El taller despliega un conjunto de contenedores conectados en red para ilustrar la recolección de métricas y la centralización de logs:

1. **api-app (FastAPI):** Servicio web de demostración que expone endpoints con latencia artificial y errores simulados.
2. **cAdvisor:** Agente colector que analiza y exporta el consumo de recursos de los contenedores Docker en ejecución.
3. **Prometheus:** Base de datos temporal (TSDB) que raspa (scrape) las métricas de la API y de cAdvisor.
4. **Loki:** Motor de agregación de logs que almacena e indexa los metadatos de los contenedores de Docker.
5. **Promtail:** Agente que recolecta las salidas de consola (logs) de Docker y las envía a Loki.
6. **Grafana:** Herramienta de visualización que conecta con Prometheus y Loki para crear dashboards interactivos.

---

## 📅 Estructura del Taller (3 Sesiones de 1 Hora)

### 🏁 Día 1: Introducción y Métricas con Prometheus
* **Teoría:** Monitoreo vs Observabilidad, M.E.L.T. (Métricas, Logs, Trazas), Modelo Pull vs Push y tipos de métricas de Prometheus (Counter, Gauge, Histogram, Summary).
* **Práctica:** Despliegue del entorno, exploración del endpoint `/metrics` en FastAPI e iniciación en PromQL con consultas sobre la API y cAdvisor.

### 🪵 Día 2: Logs Centralizados con Loki y Promtail
* **Teoría:** El problema de los logs distribuidos en entornos contenerizados, arquitectura de Loki (indexación por etiquetas vs texto completo) y sintaxis de LogQL.
* **Práctica:** Configuración del colector Promtail, generación de logs de error en FastAPI y búsqueda/filtrado avanzado de logs con LogQL en Grafana Explore.

### 📊 Día 3: Visualización con Grafana e Incidentes en Vivo
* **Teoría:** Aprovisionamiento declarativo de dashboards (Dashboard-as-Code) y las 4 Señales de Oro (Golden Signals) de Google SRE.
* **Práctica:** Construcción de un dashboard de salud de la API en Grafana y simulación de un incidente en producción para diagnosticar la causa raíz usando métricas, cAdvisor y logs de forma integrada.

---

## 🚀 Cómo empezar (Guía Rápida)

### 📋 Prerrequisitos
Asegúrate de tener instalados en tu máquina local:
* **Git**
* **Docker** y **Docker Compose**

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd taller-observabilidad
```

### 2. Levantar la infraestructura
Ejecuta el siguiente comando para construir y levantar todos los servicios en segundo plano:
```bash
docker compose up -d
```

### 3. Verificar el estado de los servicios
Puedes comprobar que los servicios están listos ejecutando `docker compose ps`. A continuación se listan las direcciones locales y puertos para cada herramienta:

| Servicio | Dirección URL | Descripción |
| :--- | :--- | :--- |
| **FastAPI API** | [http://localhost:3000](http://localhost:3000) | Aplicación FastAPI instrumentada. |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | Consola y base de datos de métricas. |
| **Grafana** | [http://localhost:3001](http://localhost:3001) | Interfaz visual (Usuario: `admin` / Password: `admin`). |
| **cAdvisor** | [http://localhost:8080](http://localhost:8080) | UI de métricas de recursos de Docker. |

---

## 🔗 Endpoints de la API FastAPI

La API simula distintos comportamientos típicos para facilitar el aprendizaje:

* **Página principal (`GET /`):** Devuelve un saludo de bienvenida simple.
* **Petición con Latencia (`GET /api/v1/data`):** Simula una llamada con latencia variable y aleatoria (entre 100ms y 500ms) para observar gráficos de latencia (percentiles) en Prometheus y Grafana.
* **Generador de Errores (`GET /api/v1/error`):** Devuelve un código HTTP 500 y escribe un log de fallo crítico en consola, simulando una excepción interna de la aplicación.
* **Métricas (`GET /metrics`):** Endpoint de recolección de métricas generado automáticamente por `prometheus-fastapi-instrumentator`.
