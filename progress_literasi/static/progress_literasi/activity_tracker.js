var inactivityTime = 0;
var maxInactivityTime = 3 * 60 * 1000; // 3 menit

function startTrackingActivity() {
    var lastMouseMoveTime = Date.now();
    var activityTimer = setInterval(function() {
        var currentTime = Date.now();
        if (currentTime - lastMouseMoveTime > maxInactivityTime) {
            // Inaktivitas lebih dari 3 menit, hentikan perhitungan waktu aktif
            clearInterval(activityTimer);
            inactivityTime = maxInactivityTime;
        } else {
            inactivityTime = currentTime - lastMouseMoveTime;
        }

        // Kirim data inaktivitas ke server dengan permintaan Ajax
        sendDataToServer(inactivityTime);
    }, 1000);

    document.addEventListener("mousemove", function() {
        lastMouseMoveTime = Date.now();
        if (inactivityTime >= maxInactivityTime) {
            // Pergerakan setelah lebih dari 3 menit inaktif, restart perhitungan waktu aktif
            inactivityTime = 0;
            startTrackingActivity();
        }
    });
}

startTrackingActivity();
