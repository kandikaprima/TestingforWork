import git

studentName = "azka"
teacherName = "kandika"

def git_pull_push(repo_path, student, teacher):
  try:
    repo = git.Repo(repo_path)

    repo.git.execute("git pull")
    repo.git.execute("git add .")
    repo.git.execute(f'''git commit -m "Add {student} Project by {teacher}"''')
    repo.git.execute("git push")

    print(f"File project {student} pada folder {repo_path} berhasil di upload")
  except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

repo_path = "D:/Koding Next/06 - Work Project/github/TestingforWork"
git_pull_push(repo_path, studentName, teacherName)