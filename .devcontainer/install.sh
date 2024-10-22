echo "Dev Container: Installing dependencies..."
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt

echo "Dev Container: Installing PostgreSQL tools..."
sudo apt update
sudo apt install -y postgresql-client

echo "Dev Container: Creating database..."
psql -U postgres -h localhost -p 5432 -c "CREATE DATABASE tacticvis_db;"

echo "Dev Container: Install complete."