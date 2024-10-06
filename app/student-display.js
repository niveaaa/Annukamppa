document.querySelectorAll('.techniques-list li').forEach(item => {
    item.addEventListener('click', function() {
        const videoFrame = this.querySelector('.video-frame');
        const iframeSrc = this.dataset.video + '?autoplay=1';

        // Check if the video frame is currently expanded or collapsed
        const isCollapsed = videoFrame.style.height === '0px' || videoFrame.style.height === '';

        // Collapse all video frames first
        document.querySelectorAll('.video-frame').forEach(frame => {
            frame.style.height = '0px';
            frame.style.paddingBottom = '0';
            frame.classList.remove('expanded'); // Remove expanded class
            frame.innerHTML = '';
        });

        // If the clicked video frame was collapsed, expand it
        if (isCollapsed) {
            const targetPaddingBottom = '56.25%'; // 16:9 aspect ratio
            videoFrame.style.paddingBottom = targetPaddingBottom;
            videoFrame.style.height = 'auto';
            videoFrame.innerHTML = `<iframe src="${iframeSrc}" allow="autoplay" allowfullscreen></iframe>`;
            videoFrame.classList.add('expanded'); // Add expanded class for margin-top
        } else {
            // If it was expanded, it's already collapsed above
            videoFrame.style.height = '0px';
            videoFrame.style.paddingBottom = '0';
            videoFrame.classList.remove('expanded'); // Ensure expanded class is removed
            videoFrame.innerHTML = '';
        }
    });
});
