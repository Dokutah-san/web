import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkeyanda"  # Diperlukan untuk flash messages

# Konfigurasi Folder Penyimpanan Gambar
UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Maksimal ukuran file 2MB

# Fungsi untuk mengecek format file gambar yang diizinkan
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Tentukan foto profil default jika pengguna belum mengunggah foto
DEFAULT_PHOTO = 'https://via.placeholder.com/150'

@app.route('/', methods=['GET', 'POST'])
def index():
    # Tentukan foto profil default jika pengguna belum mengunggah foto
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'profile_photo.jpg')):
        profile_photo_url = url_for('static', filename='img/profile_photo.jpg')
    else:
        profile_photo_url = DEFAULT_PHOTO

    # Data profil CV Anda
    profile_data = {
        "name": "Reggy Feraldin",
        "title": "Electronic Systems Engineering Student & Developer",
        "location": "Pekanbaru, Riau, Indonesia",
        "email": "email@example.com",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "photo": profile_photo_url
    }

    if request.method == 'POST':
        # Cek apakah ada file yang dikirim dalam request
        if 'photo_file' not in request.files:
            flash('Tidak ada bagian file', 'danger')
            return redirect(request.url)
        
        file = request.files['photo_file']
        
        if file.filename == '':
            flash('Anda belum memilih file', 'warning')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Kita beri nama file-nya "profile_photo.jpg" agar mudah dipanggil
            filename = 'profile_photo.jpg'
            # Simpan file ke folder static/img/
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Foto profil Anda berhasil diperbarui!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Format file tidak diizinkan! Gunakan PNG, JPG, JPEG, atau GIF.', 'danger')
            return redirect(request.url)

    return render_template('index.html', profile=profile_data)

if __name__ == '__main__':
    # Memastikan folder static/img/ sudah ada saat aplikasi jalan
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000, debug=True)        