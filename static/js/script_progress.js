// script update target_buku
document.addEventListener("DOMContentLoaded", function() {
    var updateTargetButton = document.getElementById("update-target-button");
    var resetTargetButton = document.getElementById("reset-target-button");
    var targetInputContainer = document.getElementById("target-input-container");
    var newTargetInput = document.getElementById("new-target-input");
    var saveTargetButton = document.getElementById("save-target-button");
    var targetMessage = document.getElementById("target-message");
    var closeTargetModal = document.getElementById("close-target-modal");

    // Menambahkan event listener ke tombol "Ubah Target"
    updateTargetButton.addEventListener("click", function() {
      updateTargetButton.style.display = "none";
      resetTargetButton.style.display = "none";
      targetInputContainer.style.display = "block";
    });

    // Menambahkan event listener ke tombol "Reset Target"
    resetTargetButton.addEventListener("click", function() {
      // Kirim permintaan AJAX untuk mereset target harian
      fetch("{% url 'progress_literasi:reset_target' %}", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      })
        .then(function(response) {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Gagal mereset target harian.");
          }
        })
        .then(function(data) {
          // Tampilkan pesan hasil
          targetMessage.textContent = data.message;
          // Perbarui tampilan target harian di halaman
          var targetDisplay = document.querySelector("#target-buku");
          targetDisplay.textContent = "0";
          resetTargetButton.style.display = "none";
          updateTargetButton.style.display = "block";
        })
        .catch(function(error) {
          // Tampilkan pesan kesalahan
          targetMessage.textContent = "Terjadi kesalahan: " + error.message;
        });
        targetInputContainer.style.display = "none";
        updateTargetButton.style.display = "none";
        resetTargetButton.style.display = "none";
    });
    
    // Menambahkan event listener ke tombol "Simpan"
    saveTargetButton.addEventListener("click", function() {
      var newTarget = newTargetInput.value;

      // Kirim permintaan AJAX untuk memperbarui target harian
      var formData = new FormData();
      formData.append("target_buku", newTarget);

      fetch("{% url 'progress_literasi:update_target' %}", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      })
        .then(function(response) {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Gagal memperbarui target harian.");
          }
        })
        .then(function(data) {
          // Tampilkan pesan hasil
          targetMessage.textContent = "Target harian berhasil diperbarui!";
          // Perbarui tampilan target harian di halaman
          var targetDisplay = document.querySelector("#target-buku");
          targetDisplay.textContent = newTarget;
          // Sembunyikan kembali input target setelah mengirim permintaan
          targetInputContainer.style.display = "none";
          updateTargetButton.style.display = "block";
          resetTargetButton.style.display = "block";
        })
        .catch(function(error) {
          // Tampilkan pesan kesalahan
          targetMessage.textContent = "Terjadi kesalahan: " + error.message;
        });
    });

    // Menambahkan event listener ke tombol "Close" di modal
    closeTargetModal.addEventListener("click", function() {
      targetInputContainer.style.display = "none";
      updateTargetButton.style.display = "block";
      resetTargetButton.style.display = "block";
    });

    // Fungsi untuk mendapatkan nilai token CSRF
    function getCookie(name) {
      var value = `; ${document.cookie}`;
      var parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(";").shift();
    }
  });

// script timer user
document.addEventListener("DOMContentLoaded", function() {
    var dateElement = document.getElementById("realtime-date")
    var activityElement = document.getElementById("realtime-activity");
    var userId = "{{ user.id }}";
    var loginTimestamp = localStorage.getItem("loginTimestamp_" + userId);


    // Fungsi untuk mengupdate waktu aktif sebagai timer
    function updateActivityTimer() {
      var now = new Date();
      var dateString = now.toLocaleDateString();
      var currentTime = Date.now();
      var elapsedTime = Math.floor((currentTime - loginTimestamp) / 1000); // Calculate elapsed time in seconds

      if (!loginTimestamp) {
        // Jika loginTimestamp belum ada, inisialisasi dengan waktu saat ini
        loginTimestamp = currentTime;
        localStorage.setItem("loginTimestamp_" + userId, loginTimestamp);
      }

      if (elapsedTime >= 18000) {
        // Jika lebih dari 5 jam, inisialisasi waktu dari awal
        loginTimestamp = currentTime;
        localStorage.setItem("loginTimestamp", loginTimestamp);
        elapsedTime = 0;
      }

      // Konversi waktu ke format jam:menit:detik
      var hours = Math.floor(elapsedTime / 3600);
      var minutes = Math.floor((elapsedTime % 3600) / 60);
      var seconds = elapsedTime % 60;


      // Format waktu
      var timeString = hours.toString().padStart(2, '0') + ':' +
                      minutes.toString().padStart(2, '0') + ':' +
                      seconds.toString().padStart(2, '0');
      activityElement.textContent = timeString;
      dateElement.textContent = dateString;
    }

    var timerIntervalId = setInterval(updateActivityTimer, 1000);

    function handleLogout() {
      loginTimestamp = null;
      localStorage.removeItem("loginTimestamp_" + userId);

      // Inisialisasi timer dengan waktu saat logout
      updateActivityTimer();

      // Buat interval timer baru untuk pengguna yang login kembali
      timerIntervalId = setInterval(updateActivityTimer, 1000);

    }

    var logoutButton = document.getElementById("btn-logout");
      if (logoutButton) {
        logoutButton.addEventListener("click", function() {
          console.log("logout bang")
          handleLogout();
        });
      }

    updateActivityTimer();

  });

// script riwayat buku
async function getReadingHistory() {
    return fetch("{% url 'my_profile:get_reading_history_json' %}").then((res) => res.json());
}

async function displayReadingHistory() {
    const readingHistory = await getReadingHistory();

    let htmlString = '<div class="card-row">';
    let cardCount = 0;
    readingHistory.forEach((item) => {
        const rating = item.fields.rating_count === 0 ? "No Rating" : item.fields.rating;
        console.log(item)
        htmlString += `\n<div class="card">
            <img class="card-img-top" src="https://covers.openlibrary.org/b/isbn/${item.fields.isbn}-M.jpg" alt="Card image cap" style="width: 100%; height: 200px; object-fit: cover;">
            <div class="card-body">
                <p class="card-text"><b>${item.fields.title}</b></p>
                <p class="card-text">${rating}</p>
                <a href="#" class="btn btn-primary">Detail</a>
            </div>
        </div>`;

        cardCount++;
        if (cardCount === 8) {
            htmlString += '</div><div class="card-row">';
            cardCount = 0;
        }
    });

    htmlString += '</div>';

    const bookCard = document.getElementById("book_card");
    bookCard.innerHTML = htmlString;
}

displayReadingHistory();