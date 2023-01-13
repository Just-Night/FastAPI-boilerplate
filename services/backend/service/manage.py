import typer
import subprocess

app = typer.Typer()


@app.command()
def migrate():
    subprocess.run(['bash', './scripts/migrate.sh'])


@app.command()
def check():
    subprocess.run(['bash', './scripts/check.sh'])


@app.command()
def run_server():
    print("Not work")


if __name__ == "__main__":
    app()
