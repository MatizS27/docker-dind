# Repositorio Base para Benchmark de Lenguajes

Este repositorio contiene la configuración de Docker Compose para ejecutar y comparar el rendimiento de scripts en diferentes lenguajes de programación.

## Miembros del Grupo
- Samuel Matiz Garcia [@MatizS27](https://github.com/MatizS27/docker-dind)
- Juan Felipe Santos Rodriguez [PipeJF9](https://github.com/PipeJF9)

## Enlace al Repositorio de Códigos del Benchmark
[Repositorio de Códigos](https://github.com/PipeJF9/benchmark.git)

## Instructivo para Ejecución

### Requisitos
- Docker instalado.
- Docker Compose instalado.

### Pasos para Ejecutar

1. Clona este repositorio (Habilitar el fingerprint):
   ```bash
   git clone --recurse-submodules https://github.com/MatizS27/docker-dind.git
   cd docker-dind

2. Ejecuta el compose
    ```bash
    sudo docker-compose up --build

3. Ejecuta el script para mostrar los resultados
    ```bash
    python3 generate_table.py
