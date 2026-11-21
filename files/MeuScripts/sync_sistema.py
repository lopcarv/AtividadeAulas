import subprocess

subprocess.run([
    "rsync",
    "-av",
    "--delete",
    "/home/luis/MyGit/EeTePA/sistema-escolar/",
    "/opt/lampp/htdocs/sistema-escolar/"
])

print("✅ Arquivos sincronizados com o XAMPP")