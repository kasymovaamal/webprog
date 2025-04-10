document.addEventListener('DOMContentLoaded', function() {
    // Confirm before deleting a task
    const deleteButtons = document.querySelectorAll('.btn-outline-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this task?')) {
                e.preventDefault();
            }
        });
    });

    // Date picker initialization (if using a date picker library)
    if (document.getElementById('due_date')) {
        flatpickr('#due_date', {
            dateFormat: "Y-m-d",
            minDate: "today"
        });
    }
});