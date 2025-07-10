document.addEventListener('DOMContentLoaded', function () {
    const modules = document.querySelectorAll('.dashboard-module');
    modules.forEach(module => {
        module.addEventListener('click', () => {
            module.classList.toggle('expanded');
        });
    });
});
