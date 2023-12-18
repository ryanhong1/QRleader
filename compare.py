import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Firebase 프로젝트 설정 파일 다운로드 후 경로를 지정
cred = credentials.Certificate("C:/Users/ryanh/OneDrive/바탕 화면/프로그래밍/practice-a5954-firebase-adminsdk-5tz0p-f86d8e1a79.json")

# Firebase Admin SDK 초기화
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

# 읽어올 컬렉션 이름 설정
collection_name = "product"

# 컬렉션 참조 가져오기
collection_ref = db.collection(collection_name)

# 입력 값을 받음
input_text = input("비교할 텍스트를 입력하세요: ")

# 일치 여부 확인 및 문서 삭제
docs = collection_ref.stream()
found = False

for doc in docs:
    data = doc.to_dict()
    if 'text' in data and data['text'] == input_text:
        found = True
        doc.reference.delete()  # 일치하는 문서 삭제
        break

if found:
    print("일치하는 데이터가 존재하며 삭제되었습니다.")
else:
    print("일치하는 데이터가 존재하지 않습니다.")