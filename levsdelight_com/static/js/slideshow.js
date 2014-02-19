    var slideImage = "";
    var currentSlide = 0;
    var currentPage = 1;
    var slideArray = [];
    var pagesArray = [];


    var renderPictureViewer = function(currentPage) {
        var href = currentPage[currentSlide].href
        $('.slide img').attr('src', href);
        $('.slide .title').text(currentPage[currentSlide].title);
        $('.slide .desc').text(currentPage[currentSlide].desc);

        $('.download-link a').attr('href', href)
    }
    
    // Renders the next slide in the array
    var nextSlide = function() {

    }

    // Renders the previous slide in the array
    var prevSlide = function() {

    }

    // Renders the selection in the picture viewer
    var showInViewer = function(index) {
        var dur = 400;
        var fadeBackIn = function() {
                var href = pagesArray[currentPage][index].href;
                $('.slide img').attr('src', href);
                $('.slide img').fadeTo(dur, 1);
                $('.slide .title').text(pagesArray[currentPage][index].title);
                $('.slide .desc').text(pagesArray[currentPage][index].desc);
                $('.download-link a').attr('href', href);

        };

        $('.slide img').fadeTo(dur, 0, fadeBackIn);

    }




    var renderPictureChooser = function(currentPage) {

        // Remove the current Picture Chooser before loading
        // the new one.
        $('.pictureChooser').remove();

        var pcTemplate = '<div class="pictureChooser"><ul>';

        for(var i = 0; i < currentPage.length; i++) {
            pcTemplate += '<li onClick="showInViewer('+ i +')" class="pcThumb"><img src="' +
                currentPage[i].href + '" alt="' +
                currentPage[i].title + '" /></li>';

            console.log("The title: " + currentPage[i].title);
        
        }

        pcTemplate += '</ul></div>';

        $('ul.thumbs').remove();
        $('div#thumbs').prepend(pcTemplate);

    }


    var buildSlides = function() {

        var image, aEl, caption, href, title, desc;
        var slides = [];
        var slideObj = {};
        var pageCounter = 0;
        var pages = [];
        var images = $('#thumbs').find('li');

        for (var i = 0; i < images.length; i++ ) {
            image = $(images[i]);
            aEl = $(image.children()[0]);
            caption = $(image.children()[1]);
            href = aEl.attr('href');
            title = aEl.attr('title');
            desc = caption.text();
            
            slideObj = {
                title: title,
                href: href,
                desc: desc,
            };
            slides.push(slideObj);
            slideObj = {};
        }

        console.log("The slides");
        console.log(slides);
        
        // Paginate the slides
        for(var i = 0; i < slides.length; i++) {

            if (i % 10 == 0) {
                pageCounter++;
                pages[pageCounter] = [ slides[i] ];
            } else {
                pages[pageCounter].push(slides[i])
            }
        }
        console.log(pages);
        return pages;

    }

    
    var buildPagination = function(pages) {

       // Build the pagination
       for(var i = 1;i<pages.length;i++) {
           var pageElement = '<span data-page="' + i + '" ' + 
               'class="page">' + i + '</span>';
           $('#pagination').append(pageElement);

       }

       // Set the first page as active initially.
       $('#pagination .page').first().addClass('active');


       // Setup Page Click Event Handler
       $('#pagination .page').click(function(e) {

            // First remove all active classes from page spans
            $('#pagination .page').removeClass('active');

            // Add active class to the page clicked on.
            $(this).addClass('active');

            // Get page attribute from clicked span.
            currentPage = $(this).data('page');

            //Load the new Page Array
            renderPictureChooser(pagesArray[currentPage]);
            
       });
    }


    var pagesArray = buildSlides();

    buildPagination(pagesArray);

    // Render the Picture Chooser with Page One Initially
    renderPictureChooser(pagesArray[1]);

    // Render the markup for the picture viewer
    renderPictureViewer(pagesArray[1]);

