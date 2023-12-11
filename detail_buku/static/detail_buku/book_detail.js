$("#review-form").submit(function(e) {
    e.preventDefault();  // Prevent the form from submitting normally

    var bookId = $("#book-id").val();  // Get the book ID from a hidden input
    var reviewText = $("#review-text").val();  // Get the review text from a textarea

    $.ajax({
        url: '/add_review/',
        method: 'POST',
        data: {
            'book_id': bookId,
            'review': reviewText,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            if (response.result === 'review added') {
                // The review was successfully added
                // Now update the page to display the new review
                var reviewsContainer = $("#reviews-container");
                var newReview = $("<p></p>").text(reviewText);
                reviewsContainer.append(newReview);
            }
        }
    });
});
