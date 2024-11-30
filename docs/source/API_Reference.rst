.. _API_Reference:

API Reference
=================

**API 참조**: 사용 가능한 API, 엔드포인트, 요청/응답 형식 및 사용 예제 설명. 
이 섹션은 Mind Logging API에 대한 기본 정보를 제공하며, 사용자가 API를 활용할 수 있도록 돕습니다.

### Basic Information

The Mind Logging API follows a RESTful architecture and uses JSON format for data. All requests are securely transmitted over HTTPS.

### Endpoints

1. **User Registration**
   - **URL**: `/api/register`
   - **Method**: POST
   - **Request Format**:
     ```json
     {
       "email": "user@example.com",
       "password": "your_password"
     }
     ```
   - **Response Format**:
     - Success:
       ```json
       {
         "message": "Registration successful",
         "userId": "12345"
       }
       ```
     - Failure:
       ```json
       {
         "error": "Email already exists"
       }
       ```

2. **Diary Entry Creation**
   - **URL**: `/api/diary`
   - **Method**: POST
   - **Request Format**:
     ```json
     {
       "userId": "12345",
       "content": "Today I felt happy and spent time with friends.",
       "mood": "happy",
       "photos": ["photo_url_1", "photo_url_2"]
     }
     ```
   - **Response Format**:
     - Success:
       ```json
       {
         "message": "Diary entry created",
         "entryId": "67890"
       }
       ```
     - Failure:
       ```json
       {
         "error": "Content cannot be empty"
       }
       ```

3. **Stress Logging**
   - **URL**: `/api/stress`
   - **Method**: POST
   - **Request Format**:
     ```json
     {
       "userId": "12345",
       "stressor": "studies",
       "details": "I am feeling overwhelmed with my assignments."
     }
     ```
   - **Response Format**:
     - Success:
       ```json
       {
         "message": "Stress recorded"
       }
       ```
     - Failure:
       ```json
       {
         "error": "Invalid stressor type"
       }
       ```

### Usage Examples

1. **User Registration Example**:
   ```bash
   curl -X POST https://yourapi.com/api/register \
   -H "Content-Type: application/json" \
   -d '{"email": "user@example.com", "password": "your_password"}'

2. **Diary Entry Creation Example**:
   curl -X POST https://yourapi.com/api/diary \
   -H "Content-Type: application/json" \
   -d '{"userId": "12345", "content": "Today I felt happy and spent time with friends.", "mood": "happy", "photos": ["photo_url_1", "photo_url_2"]}'

3. **Stress Logging Example**:
   curl -X POST https://yourapi.com/api/stress \
   -H "Content-Type: application/json" \
   -d '{"userId": "12345", "stressor": "studies", "details": "I am feeling overwhelmed with my assignments."}'


### 기본 정보

Mind Logging API는 RESTful 아키텍처를 따르며, JSON 형식의 데이터를 사용합니다. 모든 요청은 HTTPS를 통해 안전하게 전송됩니다.

### 엔드포인트

1. **사용자 등록**
   - **URL**: `/api/register`
   - **메서드**: POST
   - **요청 형식**:
     ```json
     {
       "email": "user@example.com",
       "password": "your_password"
     }
     ```
   - **응답 형식**:
     - 성공:
       ```json
       {
         "message": "Registration successful",
         "userId": "12345"
       }
       ```

     - 실패:
       ```json
       {
         "error": "Email already exists"
       }
       ```

2. **일기 작성**
   - **URL**: `/api/diary`
   - **메서드**: POST
   - **요청 형식**:
     ```json
     {
       "userId": "12345",
       "content": "Today I felt happy and spent time with friends.",
       "mood": "happy",
       "photos": ["photo_url_1", "photo_url_2"]
     }
     ```
   - **응답 형식**:
     - 성공:
       ```json
       {
         "message": "Diary entry created",
         "entryId": "67890"
       }
       ```

     - 실패:
       ```json
       {
         "error": "Content cannot be empty"
       }
       ```

3. **스트레스 기록**
   - **URL**: `/api/stress`
   - **메서드**: POST
   - **요청 형식**:
     ```json
     {
       "userId": "12345",
       "stressor": "studies",
       "details": "I am feeling overwhelmed with my assignments."
     }
     ```
   - **응답 형식**:
     - 성공:
       ```json
       {
         "message": "Stress recorded"
       }
       ```

     - 실패:
       ```json
       {
         "error": "Invalid stressor type"
       }
       ```

### 사용 예제

1. **사용자 등록 예제**:
   ```bash
   curl -X POST https://yourapi.com/api/register \
   -H "Content-Type: application/json" \
   -d '{"email": "user@example.com", "password": "your_password"}'

2. **일기 작성 예제**:
   curl -X POST https://yourapi.com/api/diary \
   -H "Content-Type: application/json" \
   -d '{"userId": "12345", "content": "Today I felt happy and spent time with friends.", "mood": "happy", "photos": ["photo_url_1", "photo_url_2"]}'

3. **스트레스 기록 예제**:
   curl -X POST https://yourapi.com/api/stress \
   -H "Content-Type: application/json" \
   -d '{"userId": "12345", "stressor": "studies", "details": "I am feeling overwhelmed with my assignments."}'

