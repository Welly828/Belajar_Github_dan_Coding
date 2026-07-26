// Mengambil elemen layar kalkulator dari HTML
const display = document.getElementById('display');

// Fungsi untuk menghapus layar (menjalankan tombol C)
function clearDisplay() {
    display.value = '';
}

// Fungsi untuk menambahkan angka ke layar
function appendNumber(number) {
    display.value += number;
}

// Fungsi untuk menambahkan operator matematika (+, -, *, /)
function appendOperator(operator) {
    display.value += operator;
}

// Fungsi untuk menghitung hasil (menjalankan tombol =)
function calculate() {
    try {
        // eval() adalah fungsi bawaan JavaScript yang otomatis menghitung operasi matematika
        display.value = eval(display.value);
    } catch (error) {
        // Jika ada kesalahan input (misalnya menekan tombol operator berturut-turut), tampilkan tulisan Error
        display.value = 'Error';
    }
}
