import git

def git_pull_push(repo_path, file = ".", msg = "Add new student Project"):
  """
  Melakukan git pull dan git push ke repositori yang ditentukan.

  Args:
    repo_path: Path ke direktori repositori Git.
    branch: Nama branch yang akan di-pull dan di-push.
    remote: Nama remote yang akan digunakan.
  """

  try:
    repo = git.Repo(repo_path)

    repo.git.execute("git pull")
    repo.git.execute(f"git add {file}")
    repo.git.execute(f'''git commit -m "{msg}"''')
    repo.git.execute("git push")

    print(f"Git pull dan push berhasil untuk {repo_path}")
  except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

repo_path = "D:/Koding Next/06 - Work Project/github/TestingforWork"
git_pull_push(repo_path)