import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Modify CSS to include 3D transforms for flip cards
new_style = '''
        /* Unique Gallery CSS */
        .perspective-1000 { perspective: 1000px; }
        .preserve-3d { transform-style: preserve-3d; }
        .backface-hidden { backface-visibility: hidden; }
        .my-rotate-y-180 { transform: rotateY(180deg); }
        .hand-drawn { font-family: 'Playfair Display', serif; }
'''

html = re.sub(r'<style>.*?</style>', f'<style>{new_style}</style>', html, flags=re.DOTALL)

# Extract header and footer
header_match = re.search(r'(.*?<main class="pt-20">)', html, flags=re.DOTALL)
footer_match = re.search(r'(</main>.*)', html, flags=re.DOTALL)

header = header_match.group(1)
footer = footer_match.group(1)

main_content = '''
        <!-- Hero Section -->
        <section class="py-24 md:py-32 bg-gray-50 dark:bg-gray-950 relative overflow-hidden">
            <!-- Decorative circle -->
            <div class="absolute -right-32 -top-32 w-96 h-96 bg-primary/10 rounded-full blur-3xl z-0"></div>
            
            <div class="container mx-auto px-6 md:px-12 lg:px-24 relative z-10">
                <div class="flex flex-col lg:flex-row items-center">
                    <div class="w-full lg:w-5/12 pr-0 lg:pr-12 mb-12 lg:mb-0 z-20">
                        <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block"><i class="fa-solid fa-camera mr-2"></i> Our Portfolio</span>
                        <h1 class="text-5xl md:text-7xl font-serif font-bold text-gray-900 dark:text-white mb-6">Visual Feast.</h1>
                        <p class="text-lg text-gray-600 dark:text-gray-400 mb-8 border-l-4 border-primary pl-4">
                            Immerse yourself in our visual storytelling. From empty venues to overflowing tables, see the art of grazing come to life.
                        </p>
                        <div class="flex gap-4">
                            <a href="#collections" class="btn-primary"><i class="fa-solid fa-images mr-2"></i> View Gallery</a>
                        </div>
                    </div>
                    <div class="w-full lg:w-7/12 relative">
                        <div class="absolute inset-0 bg-primary translate-x-4 translate-y-4 rounded-3xl z-0 hidden md:block"></div>
                        <img src="assets/images/gallery/signature/luxury-grazing.webp" alt="Gallery Hero" class="w-full h-[500px] object-cover rounded-3xl shadow-2xl relative z-10 border-4 border-white dark:border-gray-900">
                    </div>
                </div>
            </div>
        </section>

        <!-- 1. Signature Collections -->
        <section id="collections" class="py-24 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="text-center mb-16">
                    <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block"><i class="fa-solid fa-star mr-2"></i> Our Best</span>
                    <h2 class="text-5xl font-serif font-bold text-gray-900 dark:text-white mb-6">Signature Collections</h2>
                    <p class="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Discover our most iconic creations, from massive luxury grazing tables to intimate dessert boards.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- Item -->
                    <div class="relative group rounded-3xl overflow-hidden shadow-2xl h-96">
                        <img src="assets/images/gallery/signature/luxury-grazing.webp" alt="Luxury Grazing Table" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-8">
                            <span class="text-primary font-bold mb-2 uppercase text-xs tracking-wider">Premium Event</span>
                            <h3 class="text-3xl font-serif text-white mb-2">Luxury Grazing Tables</h3>
                            <p class="text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-4 group-hover:translate-y-0">Expansive tablescapes designed to wow your guests.</p>
                        </div>
                    </div>
                    <!-- Item -->
                    <div class="relative group rounded-3xl overflow-hidden shadow-2xl h-96">
                        <img src="assets/images/gallery/signature/artisan-cheese.webp" alt="Artisan Cheese Board" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-8">
                            <span class="text-primary font-bold mb-2 uppercase text-xs tracking-wider">Intimate Gatherings</span>
                            <h3 class="text-3xl font-serif text-white mb-2">Artisan Cheese Boards</h3>
                            <p class="text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-4 group-hover:translate-y-0">Curated selections of the finest local and imported cheeses.</p>
                        </div>
                    </div>
                    <!-- Item -->
                    <div class="relative group rounded-3xl overflow-hidden shadow-2xl h-96">
                        <img src="assets/images/gallery/signature/brunch-collection.webp" alt="Brunch Collection" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-8">
                            <span class="text-primary font-bold mb-2 uppercase text-xs tracking-wider">Morning Delight</span>
                            <h3 class="text-3xl font-serif text-white mb-2">Brunch Collections</h3>
                            <p class="text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-4 group-hover:translate-y-0">Fresh pastries, fruits, and morning favorites beautifully arranged.</p>
                        </div>
                    </div>
                    <!-- Item -->
                    <div class="relative group rounded-3xl overflow-hidden shadow-2xl h-96">
                        <img src="assets/images/gallery/signature/dessert-board.webp" alt="Dessert Board" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-8">
                            <span class="text-primary font-bold mb-2 uppercase text-xs tracking-wider">Sweet Endings</span>
                            <h3 class="text-3xl font-serif text-white mb-2">Dessert Boards</h3>
                            <p class="text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-4 group-hover:translate-y-0">Decadent chocolates, macarons, and sweet treats.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Before & After Event Transformations -->
        <section class="py-24 bg-gray-50 dark:bg-gray-950 border-y border-gray-200 dark:border-gray-800">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="mb-16 flex flex-col md:flex-row justify-between items-end pb-6">
                    <div>
                        <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-2">Venue Transformations</h2>
                        <p class="text-gray-600 dark:text-gray-400">See how we elevate empty spaces into culinary masterpieces.</p>
                    </div>
                </div>

                <div class="space-y-16">
                    <!-- Transformation 1 -->
                    <div class="flex flex-col lg:flex-row gap-8 items-center bg-white dark:bg-gray-900 p-6 md:p-8 rounded-3xl shadow-lg border border-gray-100 dark:border-gray-800">
                        <div class="w-full lg:w-1/3">
                            <h3 class="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-4">Wedding Venue</h3>
                            <p class="text-gray-600 dark:text-gray-400 mb-6">A completely blank canvas transformed into a breathtaking 15-foot focal point for a grand reception.</p>
                        </div>
                        <div class="w-full lg:w-2/3 flex flex-col md:flex-row gap-4">
                            <div class="w-full md:w-1/2 relative rounded-2xl overflow-hidden shadow-lg group">
                                <img src="assets/images/gallery/transformations/wedding-empty.webp" alt="Empty Wedding Venue" class="w-full h-64 object-cover">
                                <div class="absolute top-4 left-4 bg-black/70 text-white px-3 py-1 text-xs font-bold rounded tracking-wider">BEFORE</div>
                            </div>
                            <div class="w-full md:w-1/2 relative rounded-2xl overflow-hidden shadow-lg group border-2 border-primary">
                                <img src="assets/images/gallery/transformations/wedding-setup.webp" alt="Wedding Setup" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute top-4 left-4 bg-primary text-white px-3 py-1 text-xs font-bold rounded tracking-wider">AFTER</div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Transformation 2 -->
                    <div class="flex flex-col lg:flex-row-reverse gap-8 items-center bg-white dark:bg-gray-900 p-6 md:p-8 rounded-3xl shadow-lg border border-gray-100 dark:border-gray-800">
                        <div class="w-full lg:w-1/3">
                            <h3 class="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-4">Corporate Hall</h3>
                            <p class="text-gray-600 dark:text-gray-400 mb-6">From a sterile office lobby to a vibrant, engaging networking space.</p>
                        </div>
                        <div class="w-full lg:w-2/3 flex flex-col md:flex-row gap-4">
                            <div class="w-full md:w-1/2 relative rounded-2xl overflow-hidden shadow-lg group">
                                <img src="assets/images/gallery/transformations/corporate-empty.webp" alt="Empty Corporate Hall" class="w-full h-64 object-cover">
                                <div class="absolute top-4 left-4 bg-black/70 text-white px-3 py-1 text-xs font-bold rounded tracking-wider">BEFORE</div>
                            </div>
                            <div class="w-full md:w-1/2 relative rounded-2xl overflow-hidden shadow-lg group border-2 border-primary">
                                <img src="assets/images/gallery/transformations/corporate-setup.webp" alt="Corporate Setup" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute top-4 left-4 bg-primary text-white px-3 py-1 text-xs font-bold rounded tracking-wider">AFTER</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. Board Styling Process -->
        <section class="py-24 bg-white dark:bg-gray-900">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">The Craftsmanship</h2>
                    <p class="text-gray-600 dark:text-gray-400">Step behind the board to see how our edible art is made.</p>
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8 relative">
                    <!-- Connecting line -->
                    <div class="hidden md:block absolute top-1/2 left-0 w-full h-0.5 bg-gray-200 dark:bg-gray-800 -z-10 transform -translate-y-12"></div>
                    
                    <!-- Step 1 -->
                    <div class="text-center group">
                        <div class="w-48 h-48 mx-auto rounded-full overflow-hidden border-4 border-white dark:border-gray-800 shadow-xl mb-6 relative">
                            <img src="assets/images/gallery/process/ingredient-selection.webp" alt="Ingredient Selection" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                            <div class="absolute inset-0 bg-primary/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </div>
                        <div class="w-10 h-10 mx-auto bg-primary text-white rounded-full flex items-center justify-center font-bold mb-4 shadow-lg">1</div>
                        <h4 class="font-bold text-xl text-gray-900 dark:text-white mb-2 font-serif">Ingredient Selection</h4>
                    </div>
                    <!-- Step 2 -->
                    <div class="text-center group md:mt-12">
                        <div class="w-48 h-48 mx-auto rounded-full overflow-hidden border-4 border-white dark:border-gray-800 shadow-xl mb-6 relative">
                            <img src="assets/images/gallery/process/board-layout.webp" alt="Board Layout" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                            <div class="absolute inset-0 bg-primary/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </div>
                        <div class="w-10 h-10 mx-auto bg-primary text-white rounded-full flex items-center justify-center font-bold mb-4 shadow-lg">2</div>
                        <h4 class="font-bold text-xl text-gray-900 dark:text-white mb-2 font-serif">Board Layout</h4>
                    </div>
                    <!-- Step 3 -->
                    <div class="text-center group">
                        <div class="w-48 h-48 mx-auto rounded-full overflow-hidden border-4 border-white dark:border-gray-800 shadow-xl mb-6 relative">
                            <img src="assets/images/gallery/process/styling-garnishing.webp" alt="Styling & Garnishing" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                            <div class="absolute inset-0 bg-primary/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </div>
                        <div class="w-10 h-10 mx-auto bg-primary text-white rounded-full flex items-center justify-center font-bold mb-4 shadow-lg">3</div>
                        <h4 class="font-bold text-xl text-gray-900 dark:text-white mb-2 font-serif">Styling & Garnishing</h4>
                    </div>
                    <!-- Step 4 -->
                    <div class="text-center group md:mt-12">
                        <div class="w-48 h-48 mx-auto rounded-full overflow-hidden border-4 border-white dark:border-gray-800 shadow-xl mb-6 relative">
                            <img src="assets/images/gallery/process/final-presentation.webp" alt="Final Presentation" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                            <div class="absolute inset-0 bg-primary/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </div>
                        <div class="w-10 h-10 mx-auto bg-primary text-white rounded-full flex items-center justify-center font-bold mb-4 shadow-lg">4</div>
                        <h4 class="font-bold text-xl text-gray-900 dark:text-white mb-2 font-serif">Final Presentation</h4>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. Cheese & Pairing Spotlight -->
        <section class="py-24 bg-gray-900 text-white relative overflow-hidden">
            <div class="absolute -left-32 top-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl z-0"></div>
            
            <div class="container mx-auto px-6 md:px-12 lg:px-24 relative z-10">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-serif font-bold mb-4"><i class="fa-solid fa-wine-glass text-primary mr-3"></i>Perfect Pairings</h2>
                    <p class="text-gray-400">Discover the magic of matching the right cheese with the perfect wine.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- Card 1 -->
                    <div class="group h-[400px] perspective-1000">
                        <div class="relative h-full w-full rounded-2xl transition-all duration-700 preserve-3d group-hover:my-rotate-y-180 cursor-pointer shadow-xl border border-gray-700 bg-gray-800">
                            <!-- Front -->
                            <div class="absolute inset-0 backface-hidden w-full h-full rounded-2xl overflow-hidden">
                                <img src="assets/images/gallery/pairings/brie-chardonnay.webp" alt="Brie" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">
                                <div class="absolute bottom-0 w-full p-6 bg-gradient-to-t from-black/90 to-transparent">
                                    <h4 class="text-2xl font-serif font-bold">Brie</h4>
                                    <p class="text-primary text-sm uppercase tracking-wider mt-1">Hover for Pairing</p>
                                </div>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 my-rotate-y-180 backface-hidden w-full h-full rounded-2xl overflow-hidden bg-primary p-8 flex flex-col justify-center items-center text-center">
                                <i class="fa-solid fa-wine-bottle text-4xl mb-4 text-white/80"></i>
                                <h4 class="text-2xl font-serif font-bold text-white mb-2">Chardonnay</h4>
                                <p class="text-white/90 text-sm">The buttery notes of the Brie are beautifully complemented by the subtle oak and crisp acidity of a fine Chardonnay.</p>
                            </div>
                        </div>
                    </div>
                    <!-- Card 2 -->
                    <div class="group h-[400px] perspective-1000">
                        <div class="relative h-full w-full rounded-2xl transition-all duration-700 preserve-3d group-hover:my-rotate-y-180 cursor-pointer shadow-xl border border-gray-700 bg-gray-800">
                            <!-- Front -->
                            <div class="absolute inset-0 backface-hidden w-full h-full rounded-2xl overflow-hidden">
                                <img src="assets/images/gallery/pairings/gouda-pinot.webp" alt="Aged Gouda" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">
                                <div class="absolute bottom-0 w-full p-6 bg-gradient-to-t from-black/90 to-transparent">
                                    <h4 class="text-2xl font-serif font-bold">Aged Gouda</h4>
                                    <p class="text-primary text-sm uppercase tracking-wider mt-1">Hover for Pairing</p>
                                </div>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 my-rotate-y-180 backface-hidden w-full h-full rounded-2xl overflow-hidden bg-gray-800 border-2 border-primary p-8 flex flex-col justify-center items-center text-center">
                                <i class="fa-solid fa-wine-glass text-4xl mb-4 text-primary"></i>
                                <h4 class="text-2xl font-serif font-bold text-white mb-2">Pinot Noir</h4>
                                <p class="text-gray-300 text-sm">The nutty, caramel flavors of an aged Gouda demand the delicate red fruit complexity of a Pinot Noir.</p>
                            </div>
                        </div>
                    </div>
                    <!-- Card 3 -->
                    <div class="group h-[400px] perspective-1000">
                        <div class="relative h-full w-full rounded-2xl transition-all duration-700 preserve-3d group-hover:my-rotate-y-180 cursor-pointer shadow-xl border border-gray-700 bg-gray-800">
                            <!-- Front -->
                            <div class="absolute inset-0 backface-hidden w-full h-full rounded-2xl overflow-hidden">
                                <img src="assets/images/gallery/pairings/blue-port.webp" alt="Blue Cheese" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">
                                <div class="absolute bottom-0 w-full p-6 bg-gradient-to-t from-black/90 to-transparent">
                                    <h4 class="text-2xl font-serif font-bold">Blue Cheese</h4>
                                    <p class="text-primary text-sm uppercase tracking-wider mt-1">Hover for Pairing</p>
                                </div>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 my-rotate-y-180 backface-hidden w-full h-full rounded-2xl overflow-hidden bg-primary p-8 flex flex-col justify-center items-center text-center">
                                <i class="fa-solid fa-wine-bottle text-4xl mb-4 text-white/80"></i>
                                <h4 class="text-2xl font-serif font-bold text-white mb-2">Vintage Port</h4>
                                <p class="text-white/90 text-sm">The intense, salty punch of a rich blue cheese requires the sweet, heavy fortification of a Port to achieve harmony.</p>
                            </div>
                        </div>
                    </div>
                    <!-- Card 4 -->
                    <div class="group h-[400px] perspective-1000">
                        <div class="relative h-full w-full rounded-2xl transition-all duration-700 preserve-3d group-hover:my-rotate-y-180 cursor-pointer shadow-xl border border-gray-700 bg-gray-800">
                            <!-- Front -->
                            <div class="absolute inset-0 backface-hidden w-full h-full rounded-2xl overflow-hidden">
                                <img src="assets/images/gallery/pairings/cheddar-cabernet.webp" alt="Sharp Cheddar" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">
                                <div class="absolute bottom-0 w-full p-6 bg-gradient-to-t from-black/90 to-transparent">
                                    <h4 class="text-2xl font-serif font-bold">Sharp Cheddar</h4>
                                    <p class="text-primary text-sm uppercase tracking-wider mt-1">Hover for Pairing</p>
                                </div>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 my-rotate-y-180 backface-hidden w-full h-full rounded-2xl overflow-hidden bg-gray-800 border-2 border-primary p-8 flex flex-col justify-center items-center text-center">
                                <i class="fa-solid fa-wine-glass text-4xl mb-4 text-primary"></i>
                                <h4 class="text-2xl font-serif font-bold text-white mb-2">Cabernet Sauvignon</h4>
                                <p class="text-gray-300 text-sm">Bold, sharp cheddars need a wine that can stand up to their intensity, making the tannins of a Cabernet a perfect match.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. Client Event Stories -->
        <section class="py-24 bg-white dark:bg-gray-900">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">Event Stories</h2>
                    <p class="text-gray-600 dark:text-gray-400">Turning gatherings into unforgettable visual experiences.</p>
                </div>
                
                <div class="space-y-12">
                    <!-- Story 1 -->
                    <div class="flex flex-col lg:flex-row bg-gray-50 dark:bg-gray-950 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-800 transition-transform hover:-translate-y-2 duration-500">
                        <div class="w-full lg:w-1/2 h-80 lg:h-auto">
                            <img src="assets/images/gallery/stories/sarah-michael.webp" alt="Sarah & Michael's Wedding" class="w-full h-full object-cover">
                        </div>
                        <div class="w-full lg:w-1/2 p-8 md:p-12 flex flex-col justify-center">
                            <div class="text-primary text-sm font-bold uppercase tracking-widest mb-2">Wedding Reception</div>
                            <h3 class="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4">Sarah & Michael's Wedding</h3>
                            <ul class="space-y-2 mb-6 text-gray-600 dark:text-gray-400">
                                <li><i class="fa-solid fa-users w-6 text-primary"></i> <strong>Guest Count:</strong> 150</li>
                                <li><i class="fa-solid fa-table w-6 text-primary"></i> <strong>Board Style:</strong> 12ft Floral Integration</li>
                                <li><i class="fa-solid fa-heart w-6 text-primary"></i> <strong>Favorite Pairing:</strong> Truffle Brie & Champagne</li>
                            </ul>
                            <p class="text-gray-600 dark:text-gray-400 italic">"The grazing table was the absolute highlight of our cocktail hour. Guests are still talking about how beautiful it was!" - Sarah</p>
                        </div>
                    </div>
                    
                    <!-- Story 2 -->
                    <div class="flex flex-col lg:flex-row-reverse bg-gray-50 dark:bg-gray-950 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-800 transition-transform hover:-translate-y-2 duration-500">
                        <div class="w-full lg:w-1/2 h-80 lg:h-auto">
                            <img src="assets/images/gallery/stories/corporate-gala.webp" alt="Annual Corporate Gala" class="w-full h-full object-cover">
                        </div>
                        <div class="w-full lg:w-1/2 p-8 md:p-12 flex flex-col justify-center">
                            <div class="text-primary text-sm font-bold uppercase tracking-widest mb-2">Corporate Event</div>
                            <h3 class="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4">Annual Tech Gala</h3>
                            <ul class="space-y-2 mb-6 text-gray-600 dark:text-gray-400">
                                <li><i class="fa-solid fa-users w-6 text-primary"></i> <strong>Guest Count:</strong> 300</li>
                                <li><i class="fa-solid fa-table w-6 text-primary"></i> <strong>Board Style:</strong> Dual 15ft Symmetrical Tables</li>
                                <li><i class="fa-solid fa-heart w-6 text-primary"></i> <strong>Favorite Pairing:</strong> Aged Cheddar & Local IPA</li>
                            </ul>
                            <p class="text-gray-600 dark:text-gray-400 italic">"L'Artisan provided a sophisticated networking centerpiece that perfectly fit our brand image." - TechCorp Events Team</p>
                        </div>
                    </div>

                    <!-- Story 3 -->
                    <div class="flex flex-col lg:flex-row bg-gray-50 dark:bg-gray-950 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-800 transition-transform hover:-translate-y-2 duration-500">
                        <div class="w-full lg:w-1/2 h-80 lg:h-auto">
                            <img src="assets/images/gallery/stories/holiday-family.webp" alt="Holiday Family Event" class="w-full h-full object-cover">
                        </div>
                        <div class="w-full lg:w-1/2 p-8 md:p-12 flex flex-col justify-center">
                            <div class="text-primary text-sm font-bold uppercase tracking-widest mb-2">Private Gathering</div>
                            <h3 class="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4">The Miller's Holiday Eve</h3>
                            <ul class="space-y-2 mb-6 text-gray-600 dark:text-gray-400">
                                <li><i class="fa-solid fa-users w-6 text-primary"></i> <strong>Guest Count:</strong> 25</li>
                                <li><i class="fa-solid fa-table w-6 text-primary"></i> <strong>Board Style:</strong> Large Island Centerpiece</li>
                                <li><i class="fa-solid fa-heart w-6 text-primary"></i> <strong>Favorite Pairing:</strong> Blue Cheese & Fig Jam</li>
                            </ul>
                            <p class="text-gray-600 dark:text-gray-400 italic">"Having the board set up in our kitchen island created the perfect gathering spot. No cooking required!" - The Miller Family</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. Seasonal Inspirations -->
        <section class="py-24 bg-gray-50 dark:bg-gray-950 overflow-hidden border-y border-gray-200 dark:border-gray-800">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-2"><i class="fa-solid fa-leaf text-primary mr-3"></i>Seasonal Inspirations</h2>
                    <p class="text-gray-600 dark:text-gray-400">Ingredients dictated by the harvest.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 h-auto md:h-[600px]">
                    <!-- Spring -->
                    <div class="relative group overflow-hidden rounded-2xl md:h-full h-64">
                        <img src="assets/images/gallery/seasonal/spring-garden.webp" alt="Spring Garden Party" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-pink-900/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute bottom-8 left-8">
                            <span class="bg-white text-pink-900 px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-3 inline-block">Spring</span>
                            <h3 class="text-2xl font-serif text-white font-bold drop-shadow-md">Garden Party</h3>
                        </div>
                    </div>
                    
                    <div class="grid grid-rows-2 gap-4 h-full">
                        <!-- Summer -->
                        <div class="relative group overflow-hidden rounded-2xl h-64 md:h-full">
                            <img src="assets/images/gallery/seasonal/summer-picnic.webp" alt="Summer Picnic" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                            <div class="absolute inset-0 bg-yellow-900/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <div class="absolute bottom-6 left-6">
                                <span class="bg-white text-yellow-900 px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-2 inline-block">Summer</span>
                                <h3 class="text-xl font-serif text-white font-bold drop-shadow-md">Vineyard Picnic</h3>
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-4 h-full">
                            <!-- Autumn -->
                            <div class="relative group overflow-hidden rounded-2xl h-48 md:h-full">
                                <img src="assets/images/gallery/seasonal/autumn-harvest.webp" alt="Autumn Harvest" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-orange-900/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                <div class="absolute bottom-4 left-4">
                                    <span class="bg-white text-orange-900 px-2 py-0.5 rounded-full text-[10px] font-bold tracking-wider uppercase mb-1 inline-block">Autumn</span>
                                    <h3 class="text-lg font-serif text-white font-bold drop-shadow-md">Harvest</h3>
                                </div>
                            </div>
                            <!-- Winter -->
                            <div class="relative group overflow-hidden rounded-2xl h-48 md:h-full">
                                <img src="assets/images/gallery/seasonal/winter-holiday.webp" alt="Winter Holiday" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-blue-900/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                <div class="absolute bottom-4 left-4">
                                    <span class="bg-white text-blue-900 px-2 py-0.5 rounded-full text-[10px] font-bold tracking-wider uppercase mb-1 inline-block">Winter</span>
                                    <h3 class="text-lg font-serif text-white font-bold drop-shadow-md">Holiday</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. Behind the Scenes -->
        <section class="py-24 bg-white dark:bg-gray-900 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCI+CjxwYXRoIGQ9Ik0wIDBoNDB2NDBIMHoiIGZpbGw9Im5vbmUiLz4KPGNpcmNsZSBjeD0iMjAiIGN5PSIyMCIgcj0iMiIgZmlsbD0iIzIyMiIgZmlsbC1vcGFjaXR5PSIwLjA1Ii8+Cjwvc3ZnPg==')] dark:bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCI+CjxwYXRoIGQ9Ik0wIDBoNDB2NDBIMHoiIGZpbGw9Im5vbmUiLz4KPGNpcmNsZSBjeD0iMjAiIGN5PSIyMCIgcj0iMiIgZmlsbD0iI2ZmZiIgZmlsbC1vcGFjaXR5PSIwLjA1Ii8+Cjwvc3ZnPg==')]">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-2">Behind the Scenes</h2>
                    <p class="text-gray-600 dark:text-gray-400">The people and the passion behind every board.</p>
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 md:gap-12 pb-8">
                    <!-- Polaroid 1 -->
                    <div class="bg-white dark:bg-gray-800 p-4 pb-12 shadow-[0_10px_30px_rgba(0,0,0,0.1)] rounded-sm transform rotate-[-3deg] hover:rotate-0 transition-transform hover:z-10 relative">
                        <div class="bg-gray-200 dark:bg-gray-700 h-64 mb-4">
                            <img src="assets/images/gallery/behind-scenes/ingredient-prep.webp" alt="Ingredient Prep" class="w-full h-full object-cover">
                        </div>
                        <p class="text-center font-serif text-gray-800 dark:text-white italic text-lg hand-drawn">Early morning prep!</p>
                        <div class="absolute bottom-4 right-4 text-gray-400 dark:text-gray-500 text-xs"><i class="fa-solid fa-thumbtack"></i></div>
                    </div>
                    <!-- Polaroid 2 -->
                    <div class="bg-white dark:bg-gray-800 p-4 pb-12 shadow-[0_10px_30px_rgba(0,0,0,0.1)] rounded-sm transform rotate-[2deg] hover:rotate-0 transition-transform hover:z-10 relative mt-8 md:mt-0">
                        <div class="bg-gray-200 dark:bg-gray-700 h-64 mb-4 relative group cursor-pointer">
                            <img src="assets/images/gallery/behind-scenes/delivery-setup.webp" alt="Delivery Setup" class="w-full h-full object-cover">
                            <!-- Video Play Overlay -->
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                                <div class="w-16 h-16 bg-primary/90 text-white rounded-full flex items-center justify-center shadow-lg"><i class="fa-solid fa-play text-xl ml-1"></i></div>
                            </div>
                        </div>
                        <p class="text-center font-serif text-gray-800 dark:text-white italic text-lg hand-drawn">Loading in the 15-footer.</p>
                    </div>
                    <!-- Polaroid 3 -->
                    <div class="bg-white dark:bg-gray-800 p-4 pb-12 shadow-[0_10px_30px_rgba(0,0,0,0.1)] rounded-sm transform rotate-[-1deg] hover:rotate-0 transition-transform hover:z-10 relative mt-8 md:mt-12">
                        <div class="bg-gray-200 dark:bg-gray-700 h-64 mb-4">
                            <img src="assets/images/gallery/behind-scenes/team-moments.webp" alt="Team Moments" class="w-full h-full object-cover">
                        </div>
                        <p class="text-center font-serif text-gray-800 dark:text-white italic text-lg hand-drawn">The dream team ♥️</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. Social Media Moments -->
        <section class="py-24 bg-gray-50 dark:bg-gray-950 border-t border-gray-200 dark:border-gray-800">
            <div class="container mx-auto px-6 md:px-12 lg:px-24">
                <div class="flex flex-col lg:flex-row gap-12 items-center">
                    <div class="w-full lg:w-1/3">
                        <h2 class="text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">Share The Love</h2>
                        <p class="text-gray-600 dark:text-gray-400 mb-8">Follow us on Instagram for daily inspiration and tag us in your event photos to be featured.</p>
                        
                        <div class="flex flex-col gap-3">
                            <span class="text-primary font-medium hover:underline cursor-pointer">#ArtOfGrazing</span>
                            <span class="text-primary font-medium hover:underline cursor-pointer">#LuxuryCharcuterie</span>
                            <span class="text-primary font-medium hover:underline cursor-pointer">#CheeseBoardGoals</span>
                            <span class="text-primary font-medium hover:underline cursor-pointer">#GatherAndGraze</span>
                            <span class="text-primary font-medium hover:underline cursor-pointer">#GrazingTableInspiration</span>
                        </div>
                        
                        <a href="#" class="mt-8 btn-primary inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow @LArtisan</a>
                    </div>
                    
                    <div class="w-full lg:w-2/3">
                        <div class="grid grid-cols-2 md:grid-cols-3 gap-2 md:gap-4">
                            <!-- Gram 1 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-1.webp" alt="Social 1" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 245</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 12</span>
                                </div>
                            </div>
                            <!-- Gram 2 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-2.webp" alt="Social 2" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 892</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 44</span>
                                </div>
                            </div>
                            <!-- Gram 3 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-3.webp" alt="Social 3" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 120</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 3</span>
                                </div>
                            </div>
                            <!-- Gram 4 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-4.webp" alt="Social 4" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 430</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 18</span>
                                </div>
                            </div>
                            <!-- Gram 5 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-5.webp" alt="Social 5" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 566</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 29</span>
                                </div>
                            </div>
                            <!-- Gram 6 -->
                            <div class="relative group aspect-square overflow-hidden rounded-xl bg-gray-200 dark:bg-gray-800">
                                <img src="assets/images/gallery/social/social-6.webp" alt="Social 6" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                                    <span class="text-white font-bold"><i class="fa-solid fa-heart mr-1"></i> 321</span>
                                    <span class="text-white font-bold"><i class="fa-solid fa-comment mr-1"></i> 8</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

new_html = header + '<main class="pt-20">\n' + main_content + '\n' + footer

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('gallery.html rewritten successfully.')
