# Лабораторна робота 1
> Виконав: Грибенко Єгор, ІМ-31мн

### Docker-compose:

```yml
services:

  nginx-api:
    container_name: lb-api
    image: nginx:latest
    volumes:
      - ./api/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - api-1
      - api-2
    ports:
      - "5000:5000"

  api-1:
    container_name: api-1
    build: ./api
    environment:
      - FLASK_ENV=development
    volumes:
      - ./api:/app

  api-2:
    container_name: api-2
    build: ./api
    environment:
      - FLASK_ENV=development
    volumes:
      - ./api:/app

  lb-provider:
    container_name: lb-provider
    image: nginx:latest
    volumes:
      - ./service/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - provider-1
      - provider-2

  provider-1:
    container_name: provider-1
    build: ./service
    environment:
      - FLASK_ENV=development
    volumes:
      - ./service:/app

  provider-2:
    container_name: provider-2
    build: ./service
    environment:
      - FLASK_ENV=development
    volumes:
      - ./service:/app

```

### Перевірка балансувальника:
![image](https://github.com/user-attachments/assets/fa0be418-c3aa-459e-bde1-259edc2cc0ab)

### Перевірка роботи проекту при падінні апі-1 та провайдера-2:
![image](https://github.com/user-attachments/assets/189911fd-f520-4b53-994b-5801919896a7)

Як результат, конекшн направляється через апі-2 та провайдера-1.

---
