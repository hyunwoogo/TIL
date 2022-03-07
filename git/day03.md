### Branch

- 독립적인 공간
- master와 같은 내용을 가지고 뻗어나옴
- 완전히 작업을 완료한 후에 master로 추가된다. (merge)
- 상용, 배포, 서비스 운영 중인 master에서 작업할 수 없기 때문에 사용한다.

1. git branch

- 브랜치 조회, 생성, 삭제 관련 명령어

```bash
# 브랜치 목록 확인
git branch

# 브랜치 생성
git branch 신규브랜치명

# 브랜치 삭제
git branch -d 브랜치명	# merge하지 않은 브랜치는 이 명령어로 삭제 되지 X
git branch -D 브랜치명	# 강제삭제 옵션
```

2. git switch

- 다른 브랜치로 이동하는 명령어

```bash
# 브랜치 이동
git switch 이동할 브랜치 명

# 브랜치 생성 후 이동
git switch -c 브랜치명
```

---

- 브랜치 사용 예제

```bash
mkdir git_branch_practice	# 폴더생성
cd git_branch_practice	# 생성한 폴더로 이동
touch README.md		# README파일 생성
git init
git add .	# 변경된 사항들 모두 추가
git commit -m "initial README.md-master"

# README.md에 다시 내용 작성 후 저장
git add . 
git commit -m "update README.md-master"


git branch	# 브랜치 목록 확인
git branch hotfix	# hotfix 브랜치 생성
git switch hotfix	# hotfix 브랜치로 이동

touch a.txt	# 새파일 생성

git add.
git status
git commit -m "update README-hotfix"
git switch master	# hotfix에서 작성한것들이 모두 사라짐


```

