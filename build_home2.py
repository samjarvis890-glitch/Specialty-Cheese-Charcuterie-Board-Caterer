import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Find the head and header/nav part
head_nav_match = re.search(r'(.*?<!-- Main Content -->\s*<main class="[^"]*">)', index_html, re.DOTALL)
if head_nav_match:
    head_nav = head_nav_match.group(1)
else:
    head_nav = "<!-- Error extracting head and nav -->"

# Find the footer part
footer_match = re.search(r'(<!-- Footer -->.*)', index_html, re.DOTALL)
if footer_match:
    footer = footer_match.group(1)
else:
    footer = "<!-- Error extracting footer -->"

main_content = """
        <!-- 1. Hero Builder Section -->
        <section class="relative h-[90vh] min-h-[600px] flex items-center justify-center bg-gray-900 overflow-hidden">
            <div class="absolute inset-0 z-0">
                <img src="assets/images/home2/hero-builder.webp" alt="Luxury charcuterie board builder" loading="lazy" class="w-full h-full object-cover opacity-50">
            </div>
            <div class="relative z-10 text-center px-6 md:px-12 lg:px-24 max-w-4xl mx-auto">
                <span class="text-primary font-semibold tracking-wider uppercase text-sm mb-4 block">Interactive Experience</span>
                <h1 class="text-4xl md:text-6xl font-serif text-white font-bold mb-6 tracking-wide">
                    Design Your Perfect Charcuterie Board
                </h1>
                <p class="text-lg md:text-xl text-gray-200 mb-10 max-w-2xl mx-auto font-light">
                    Customize your luxury grazing experience. Select your event type, guest count, and artisan ingredients for an instant live quote.
                </p>
                <div class="flex flex-col sm:flex-row justify-center gap-4">
                    <a href="#event-type" class="btn-primary py-3 px-8 text-lg shadow-lg hover:shadow-xl"><i class="fa-solid fa-wand-magic-sparkles mr-2"></i> Start Building</a>
                </div>
            </div>
        </section>

        <!-- 2. Event Type Selector -->
        <section id="event-type" class="py-20 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
            <div class="container mx-auto max-w-[1200px] px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">Select Your Event Type</h2>
                    <p class="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Different occasions call for different aesthetic spreads. Tell us what you're celebrating.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    <!-- Event Cards -->
                    <div class="event-card cursor-pointer group rounded-xl overflow-hidden border-2 border-transparent hover:border-primary transition-all shadow-md dark:bg-gray-800 dark:border-gray-700 bg-gray-50" onclick="selectEvent('Wedding')">
                        <div class="h-40 overflow-hidden relative">
                            <img src="assets/images/home2/event-wedding.webp" alt="Wedding" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
                        </div>
                        <div class="p-5 text-center">
                            <h3 class="font-serif font-semibold text-xl text-gray-900 dark:text-white">Wedding</h3>
                            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Elegant & Expansive</p>
                        </div>
                    </div>
                    
                    <div class="event-card cursor-pointer group rounded-xl overflow-hidden border-2 border-transparent hover:border-primary transition-all shadow-md dark:bg-gray-800 dark:border-gray-700 bg-gray-50" onclick="selectEvent('Corporate')">
                        <div class="h-40 overflow-hidden relative">
                            <img src="assets/images/home2/event-corporate.webp" alt="Corporate" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
                        </div>
                        <div class="p-5 text-center">
                            <h3 class="font-serif font-semibold text-xl text-gray-900 dark:text-white">Corporate</h3>
                            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Professional & Impressive</p>
                        </div>
                    </div>
                    
                    <div class="event-card cursor-pointer group rounded-xl overflow-hidden border-2 border-transparent hover:border-primary transition-all shadow-md dark:bg-gray-800 dark:border-gray-700 bg-gray-50" onclick="selectEvent('Birthday')">
                        <div class="h-40 overflow-hidden relative">
                            <img src="assets/images/home2/event-birthday.webp" alt="Birthday" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
                        </div>
                        <div class="p-5 text-center">
                            <h3 class="font-serif font-semibold text-xl text-gray-900 dark:text-white">Birthday Party</h3>
                            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Fun & Abundant</p>
                        </div>
                    </div>
                    
                    <div class="event-card cursor-pointer group rounded-xl overflow-hidden border-2 border-transparent hover:border-primary transition-all shadow-md dark:bg-gray-800 dark:border-gray-700 bg-gray-50" onclick="selectEvent('Intimate')">
                        <div class="h-40 overflow-hidden relative">
                            <img src="assets/images/home2/event-intimate.webp" alt="Intimate" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
                        </div>
                        <div class="p-5 text-center">
                            <h3 class="font-serif font-semibold text-xl text-gray-900 dark:text-white">Intimate Gathering</h3>
                            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Cozy & Curated</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. Guest Count Planner -->
        <section id="guest-count" class="py-20 bg-gray-50 dark:bg-gray-950 border-b border-gray-200 dark:border-gray-800">
            <div class="container mx-auto max-w-[1400px] px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24">
                <div class="flex flex-col lg:flex-row items-center gap-12">
                    <div class="w-full lg:w-1/2">
                        <img src="assets/images/home2/guest-planner.webp" alt="Guest Planner" class="rounded-2xl shadow-xl w-full object-cover h-[400px]">
                    </div>
                    <div class="w-full lg:w-1/2">
                        <h2 class="text-3xl md:text-4xl font-serif font-bold text-gray-900 dark:text-white mb-6">Plan for Your Guests</h2>
                        <p class="text-gray-600 dark:text-gray-400 mb-8">
                            Whether you're hosting an intimate party of 10 or a grand reception for 300, we ensure there is an abundance of premium artisan food for everyone.
                        </p>
                        
                        <div class="bg-white dark:bg-gray-800 p-8 rounded-xl shadow-lg border border-gray-100 dark:border-gray-700">
                            <label for="guestSlider" class="flex justify-between items-center mb-4 text-lg font-medium text-gray-900 dark:text-white">
                                <span>Number of Guests:</span>
                                <span id="guestCountDisplay" class="text-2xl font-bold text-primary">50</span>
                            </label>
                            <input type="range" id="guestSlider" min="10" max="300" step="5" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700 accent-primary" oninput="updateGuestCount(this.value)">
                            
                            <div class="flex justify-between text-sm text-gray-500 dark:text-gray-400 mt-3">
                                <span>10 (Min)</span>
                                <span>300+</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. & 5. Interactive Board Configurator & Live Price -->
        <section id="configurator" class="py-20 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
            <div class="container mx-auto max-w-[1400px] px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24">
                <div class="text-center mb-16">
                    <h2 class="text-3xl md:text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">Interactive Board Configurator</h2>
                    <p class="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Select your artisan cheeses, premium cured meats, and gourmet accompaniments.</p>
                </div>
                
                <div class="flex flex-col lg:flex-row gap-12">
                    <!-- Configurator Options -->
                    <div class="w-full lg:w-2/3 space-y-8">
                        <div class="relative rounded-2xl overflow-hidden shadow-lg h-[300px] mb-8">
                            <img src="assets/images/home2/board-config.webp" alt="Board Config" class="w-full h-full object-cover">
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <!-- Cheese Selection -->
                            <div>
                                <h3 class="text-xl font-serif font-semibold text-gray-900 dark:text-white mb-4 border-b border-gray-200 dark:border-gray-700 pb-2">Artisan Cheeses</h3>
                                <div class="space-y-3">
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()" checked>
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Aged Cheddar & Brie</span>
                                    </label>
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()" checked>
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Truffle Gouda (+/guest)</span>
                                    </label>
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()">
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Gorgonzola Dolce</span>
                                    </label>
                                </div>
                            </div>
                            
                            <!-- Charcuterie Selection -->
                            <div>
                                <h3 class="text-xl font-serif font-semibold text-gray-900 dark:text-white mb-4 border-b border-gray-200 dark:border-gray-700 pb-2">Premium Meats</h3>
                                <div class="space-y-3">
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()" checked>
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Prosciutto di Parma</span>
                                    </label>
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()" checked>
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Spicy Soppressata</span>
                                    </label>
                                    <label class="flex items-center space-x-3 cursor-pointer group">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary dark:bg-gray-800 dark:border-gray-600" onchange="calculatePrice()">
                                        <span class="text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Wagyu Bresaola (+/guest)</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Live Price Estimator -->
                    <div class="w-full lg:w-1/3">
                        <div class="sticky top-24 bg-gray-50 dark:bg-gray-800 rounded-2xl shadow-xl overflow-hidden border border-gray-200 dark:border-gray-700">
                            <div class="h-32 overflow-hidden relative">
                                <img src="assets/images/home2/live-price.webp" alt="Live Price" class="w-full h-full object-cover opacity-80">
                                <div class="absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent flex items-end p-6">
                                    <h3 class="font-serif text-2xl font-bold text-white">Your Estimate</h3>
                                </div>
                            </div>
                            
                            <div class="p-6 space-y-4">
                                <div class="flex justify-between text-gray-600 dark:text-gray-300">
                                    <span>Base Package (50 Guests)</span>
                                    <span id="basePriceDisplay"></span>
                                </div>
                                <div class="flex justify-between text-gray-600 dark:text-gray-300">
                                    <span>Premium Upgrades</span>
                                    <span id="upgradePriceDisplay"></span>
                                </div>
                                <div class="border-t border-gray-200 dark:border-gray-700 pt-4 mt-4 flex justify-between items-center">
                                    <span class="text-xl font-bold text-gray-900 dark:text-white">Total</span>
                                    <span id="totalPriceDisplay" class="text-3xl font-serif font-bold text-primary"></span>
                                </div>
                                <p class="text-xs text-gray-500 text-center mt-4">*This is an estimate. Final pricing may vary based on seasonal availability.</p>
                                
                                <button class="w-full btn-primary py-3 mt-4" onclick="document.getElementById('reservation').scrollIntoView();">
                                    Continue to Reservation
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5b. Sommelier Wine & Cheese Pairing Guide -->
        <section id="pairing-guide" class="py-20 bg-gray-50 dark:bg-gray-950 border-b border-gray-200 dark:border-gray-800">
            <div class="container mx-auto max-w-[1400px] px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24">
                <div class="text-center mb-16">
                    <span class="text-primary font-semibold tracking-wider uppercase text-sm mb-4 block">Interactive Experience</span>
                    <h2 class="text-3xl md:text-4xl font-serif font-bold text-gray-900 dark:text-white mb-4">Artisan Savor & Wine Matcher</h2>
                    <p class="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Explore how our hand-selected cheeses harmonize with the finest wines and gourmet accompaniments. Select a cheese profile below to see the sommelier's choice.</p>
                </div>

                <div class="flex flex-col lg:flex-row gap-12 items-stretch">
                    <!-- Tab Navigation & Description -->
                    <div class="w-full lg:w-1/2 flex flex-col justify-between">
                        <div class="space-y-4">
                            <h3 class="text-2xl font-serif font-semibold text-gray-900 dark:text-white mb-6">Select a Cheese Style</h3>
                            <div class="grid grid-cols-2 gap-4">
                                <!-- Tab Buttons -->
                                <button onclick="selectPairing('creamy')" id="btn-creamy" class="pairing-tab-btn flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-left transition-all duration-300 shadow-sm hover:shadow-md hover:border-primary/50 text-gray-900 dark:text-white ring-2 ring-primary border-primary">
                                    <div class="w-10 h-10 rounded-lg bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary">
                                        <i class="fa-solid fa-cloud"></i>
                                    </div>
                                    <div>
                                        <span class="block font-bold text-sm">Rich & Creamy</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Brie, Camembert</span>
                                    </div>
                                </button>

                                <button onclick="selectPairing('aged')" id="btn-aged" class="pairing-tab-btn flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-left transition-all duration-300 shadow-sm hover:shadow-md hover:border-primary/50 text-gray-900 dark:text-white">
                                    <div class="w-10 h-10 rounded-lg bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary">
                                        <i class="fa-solid fa-shield-halved"></i>
                                    </div>
                                    <div>
                                        <span class="block font-bold text-sm">Sharp & Aged</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Cheddar, Gouda</span>
                                    </div>
                                </button>

                                <button onclick="selectPairing('bold')" id="btn-bold" class="pairing-tab-btn flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-left transition-all duration-300 shadow-sm hover:shadow-md hover:border-primary/50 text-gray-900 dark:text-white">
                                    <div class="w-10 h-10 rounded-lg bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary">
                                        <i class="fa-solid fa-droplet"></i>
                                    </div>
                                    <div>
                                        <span class="block font-bold text-sm">Bold & Blue</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Gorgonzola, Stilton</span>
                                    </div>
                                </button>

                                <button onclick="selectPairing('tangy')" id="btn-tangy" class="pairing-tab-btn flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-left transition-all duration-300 shadow-sm hover:shadow-md hover:border-primary/50 text-gray-900 dark:text-white">
                                    <div class="w-10 h-10 rounded-lg bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary">
                                        <i class="fa-solid fa-lemon"></i>
                                    </div>
                                    <div>
                                        <span class="block font-bold text-sm">Fresh & Tangy</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Goat, Feta, Burrata</span>
                                    </div>
                                </button>
                            </div>
                        </div>

                        <!-- Description & Details -->
                        <div class="mt-8 bg-white dark:bg-gray-900 p-8 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm flex-grow flex flex-col justify-between">
                            <div>
                                <h4 id="pairing-title" class="text-xl font-serif font-bold text-gray-900 dark:text-white mb-3">Rich & Creamy Cheese Profile</h4>
                                <p id="pairing-desc" class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed mb-6">
                                    Soft-ripened cheeses feature a luxurious, buttery texture and subtle earthy undertones. They require crisp whites or light, fruity reds to cut through the rich butterfat and cleanse the palate.
                                </p>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-gray-100 dark:border-gray-800">
                                <div>
                                    <h5 class="text-xs uppercase tracking-wider font-bold text-primary mb-2">Ideal Meat Accompaniment</h5>
                                    <p id="pairing-meat" class="text-sm font-semibold text-gray-900 dark:text-white">Prosciutto di Parma or Sweet Coppa</p>
                                </div>
                                <div>
                                    <h5 class="text-xs uppercase tracking-wider font-bold text-primary mb-2">Sweet & Savory Extras</h5>
                                    <p id="pairing-extras" class="text-sm font-semibold text-gray-900 dark:text-white">Fresh Figs, Raw Honeycomb, Marcona Almonds</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Sommelier's Recommendation Card -->
                    <div class="w-full lg:w-1/2">
                        <div class="h-full bg-white dark:bg-gray-900 rounded-3xl border border-gray-200 dark:border-gray-800 shadow-lg overflow-hidden flex flex-col justify-between">
                            <div class="relative h-64 md:h-72 overflow-hidden">
                                <img id="pairing-img" src="assets/images/wine-pairings/pairing_guide.webp" alt="Wine Pairing Guide" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent flex items-end p-8">
                                    <div>
                                        <span class="text-xs uppercase tracking-widest font-bold text-primary bg-white/90 dark:bg-gray-900/90 px-3 py-1 rounded-full mb-2 inline-block">Sommelier Choice</span>
                                        <h3 id="pairing-wine-title" class="font-serif text-2xl font-bold text-white">Chardonnay or Pinot Noir</h3>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="p-8 space-y-6 flex-grow flex flex-col justify-between">
                                <div class="space-y-4">
                                    <div class="flex items-start gap-4">
                                        <div class="w-10 h-10 rounded-full bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary flex-shrink-0">
                                            <i class="fa-solid fa-wine-glass-empty"></i>
                                        </div>
                                        <div>
                                            <h4 class="font-bold text-gray-900 dark:text-white text-base">Why It Works</h4>
                                            <p id="pairing-why" class="text-xs text-gray-500 dark:text-gray-400 mt-1 leading-relaxed">
                                                A high-acid, unoaked Chardonnay cuts right through the luxurious creaminess, while a delicate Pinot Noir provides bright red berry notes that complement the mild, milky flavors without overpowering them.
                                            </p>
                                        </div>
                                    </div>

                                    <div class="flex items-start gap-4">
                                        <div class="w-10 h-10 rounded-full bg-primary/10 dark:bg-primary/20 flex items-center justify-center text-primary flex-shrink-0">
                                            <i class="fa-solid fa-temperature-half"></i>
                                        </div>
                                        <div>
                                            <h4 class="font-bold text-gray-900 dark:text-white text-base">Serving Tip</h4>
                                            <p id="pairing-tip" class="text-xs text-gray-500 dark:text-gray-400 mt-1 leading-relaxed">
                                                Serve the cheese at room temperature (let it sit out for 30-45 minutes before serving) so it gets beautifully runny and releases its full aromatic profile.
                                            </p>
                                        </div>
                                    </div>
                                </div>

                                <div class="pt-6 border-t border-gray-100 dark:border-gray-800 text-center">
                                    <a href="wine-pairings.html" class="inline-flex items-center text-primary font-semibold hover:underline">
                                        Explore Wine Pairing Matrix <i class="fa-solid fa-arrow-right ml-2"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. Reservation Calendar CTA -->
        <section id="reservation" class="py-20 bg-gray-900 relative overflow-hidden">
            <div class="absolute inset-0 z-0">
                <img src="assets/images/home2/reservation-calendar.webp" alt="Reservation Calendar" loading="lazy" class="w-full h-full object-cover opacity-30">
            </div>
            <div class="container mx-auto max-w-[1400px] px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24 relative z-10">
                <div class="bg-white/10 dark:bg-black/40 backdrop-blur-md rounded-3xl border border-white/20 p-8 md:p-12 max-w-4xl mx-auto shadow-2xl">
                    <div class="text-center mb-10">
                        <h2 class="text-3xl md:text-4xl font-serif font-bold text-white mb-4">Secure Your Date</h2>
                        <p class="text-gray-300">Our calendar fills up quickly. Request your reservation now to guarantee availability for your event.</p>
                    </div>
                    
                    <form class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-white mb-2">Event Date</label>
                                <input type="date" class="w-full bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-white mb-2">Event Time</label>
                                <input type="time" class="w-full bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-white mb-2">Full Name</label>
                                <input type="text" placeholder="John Doe" class="w-full bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-white mb-2">Email Address</label>
                                <input type="email" placeholder="john@example.com" class="w-full bg-white/20 border border-white/30 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent">
                            </div>
                        </div>
                        <div class="text-center pt-4">
                            <button type="submit" class="btn-primary py-4 px-12 text-lg shadow-[0_0_15px_rgba(212,175,55,0.4)] hover:shadow-[0_0_25px_rgba(212,175,55,0.6)]">
                                Request Booking
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- Custom Script for Home 2 Logic -->
    <script>
        // Event Type Selection
        function selectEvent(type) {
            const cards = document.querySelectorAll('.event-card');
            cards.forEach(card => {
                card.classList.remove('border-primary', 'ring-2', 'ring-primary');
                card.classList.add('border-transparent');
            });
            event.currentTarget.classList.remove('border-transparent');
            event.currentTarget.classList.add('border-primary', 'ring-2', 'ring-primary');
        }

        // Price Calculation Logic
        let currentGuests = 50;
        const BASE_RATE = 15; //  per guest
        
        function updateGuestCount(val) {
            currentGuests = parseInt(val);
            document.getElementById('guestCountDisplay').innerText = currentGuests;
            calculatePrice();
        }

        function calculatePrice() {
            const checkboxes = document.querySelectorAll('.form-checkbox');
            let upgradeCostPerGuest = 0;
            
            // Check Truffle Gouda
            if(checkboxes[1].checked) upgradeCostPerGuest += 2;
            // Check Wagyu Bresaola
            if(checkboxes[5].checked) upgradeCostPerGuest += 3;
            
            const basePrice = currentGuests * BASE_RATE;
            const upgradePrice = currentGuests * upgradeCostPerGuest;
            const total = basePrice + upgradePrice;
            
            document.getElementById('basePriceDisplay').innerText = '$' + basePrice;
            document.getElementById('upgradePriceDisplay').innerText = '$' + upgradePrice;
            document.getElementById('totalPriceDisplay').innerText = '$' + total;
            
            // Update Base Package text
            const baseText = document.querySelector('#basePriceDisplay').previousElementSibling;
            baseText.innerText = 'Base Package (' + currentGuests + ' Guests)';
        }

        // Pairing Selector Logic
        const PAIRING_DATA = {
            creamy: {
                title: "Rich & Creamy Cheese Profile",
                desc: "Soft-ripened cheeses feature a luxurious, buttery texture and subtle earthy undertones. They require crisp whites or light, fruity reds to cut through the rich butterfat and cleanse the palate.",
                meat: "Prosciutto di Parma or Sweet Coppa",
                extras: "Fresh Figs, Raw Honeycomb, Marcona Almonds",
                wineTitle: "Chardonnay or Pinot Noir",
                why: "A high-acid, unoaked Chardonnay cuts right through the luxurious creaminess, while a delicate Pinot Noir provides bright red berry notes that complement the mild, milky flavors without overpowering them.",
                tip: "Serve the cheese at room temperature (let it sit out for 30-45 minutes before serving) so it gets beautifully runny and releases its full aromatic profile.",
                img: "assets/images/wine-pairings/pairing_guide.webp"
            },
            aged: {
                title: "Sharp & Aged Cheese Profile",
                desc: "As cheeses age, they lose moisture and develop crystalline textures with deep, savory, and nutty flavors. They pair best with full-bodied reds or oxidized whites that match their bold intensity.",
                meat: "Spicy Soppressata or Jamón Ibérico",
                extras: "Cavalier Walnuts, Dried Apricots, Grainy Mustard",
                wineTitle: "Cabernet Sauvignon or Sherry",
                why: "The bold tannins in Cabernet Sauvignon bind with the protein and fat of aged cheese, softening the wine and bringing out rich, nutty, and caramelized tones in both.",
                tip: "Aged cheese can be crumbled rather than sliced to accentuate its natural crystalline structure and crunch.",
                img: "assets/images/wine-pairings/cheese_matrix.webp"
            },
            bold: {
                title: "Bold & Blue Cheese Profile",
                desc: "Blue cheeses are famously intense, salty, and metallic with a creamy, crumbly bite. They need sweet wines or dessert styles to create a classic sweet-and-savory contrast.",
                meat: "Peppered Salami or Roast Beef Slices",
                extras: "Candied Pecans, Bosc Pear Slices, Dark Chocolate",
                wineTitle: "Sauternes, Port, or Stout Beer",
                why: "The sweetness of Port or Sauternes balances the intense saltiness of the blue veins, transforming what could be an overwhelming bite into a harmonious, dessert-like delicacy.",
                tip: "Use a dedicated cheese wire or clean knife for blue cheese to avoid transferring blue mold spores to other cheeses on your board.",
                img: "assets/images/wine-pairings/expert_picks.webp"
            },
            tangy: {
                title: "Fresh & Tangy Cheese Profile",
                desc: "Fresh cheeses are unripened, soft, and moist, offering bright, milky, and acidic profiles. They pair perfectly with vibrant, herbaceous whites or sparkling wines.",
                meat: "Bresaola or Prosciutto Cotto",
                extras: "Green Olives, Roasted Pistachios, Fresh Basil",
                wineTitle: "Sauvignon Blanc or Prosecco",
                why: "The herbaceous and citrusy notes of Sauvignon Blanc match the grassy notes of goat cheese, while the high acidity of both creates a refreshing, mouth-watering pairing.",
                tip: "Fresh goat cheese can be rolled in herbs, cracked black pepper, or edible flowers to add color and complexity to your spread.",
                img: "assets/images/wine-pairings/expert_picks2.webp"
            }
        };

        function selectPairing(style) {
            // Update Active Tab Button Styles
            const buttons = document.querySelectorAll('.pairing-tab-btn');
            buttons.forEach(btn => {
                btn.classList.remove('ring-2', 'ring-primary', 'border-primary');
            });
            
            const activeBtn = document.getElementById('btn-' + style);
            if (activeBtn) {
                activeBtn.classList.add('ring-2', 'ring-primary', 'border-primary');
            }

            // Update Content
            const titleEl = document.getElementById('pairing-title');
            const descEl = document.getElementById('pairing-desc');
            const meatEl = document.getElementById('pairing-meat');
            const extrasEl = document.getElementById('pairing-extras');
            const wineTitleEl = document.getElementById('pairing-wine-title');
            const whyEl = document.getElementById('pairing-why');
            const tipEl = document.getElementById('pairing-tip');
            const imgEl = document.getElementById('pairing-img');

            const data = PAIRING_DATA[style];
            if (data) {
                titleEl.innerText = data.title;
                descEl.innerText = data.desc;
                meatEl.innerText = data.meat;
                extrasEl.innerText = data.extras;
                wineTitleEl.innerText = data.wineTitle;
                whyEl.innerText = data.why;
                tipEl.innerText = data.tip;
                imgEl.src = data.img;
            }
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            // Select first event by default
            document.querySelector('.event-card').click();
            calculatePrice();
        });
    </script>
"""

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(head_nav)
    f.write(main_content)
    f.write('\\n')
    f.write(footer)

print('home2.html built successfully.')
