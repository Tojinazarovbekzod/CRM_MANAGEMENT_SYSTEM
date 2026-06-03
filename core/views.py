from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from .forms import RegisterForm


def health(request):
    return JsonResponse({'status': 'ok'})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.first_name} {user.last_name}!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.username}!")
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, "Username yoki parol noto'g'ri.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Tizimdan chiqildi.")
    return redirect('home')


def home(request):
    context = {
        'stats': [
            {'number': '500+', 'label': 'Daily Guests'},
            {'number': '25+', 'label': 'Coffee Origins'},
            {'number': '13', 'label': 'Years of Love'},
            {'number': '4.9★', 'label': 'Average Rating'},
        ],
        'features': [
            {
                'icon': '🌱',
                'title': 'Ethically Sourced',
                'description': 'Every bean is sourced directly from farmers who practice sustainable, fair-trade agriculture across Ethiopia, Colombia, and Guatemala.',
            },
            {
                'icon': '☕',
                'title': 'Expert Baristas',
                'description': 'Our baristas train for months before serving their first cup. They are artists, and espresso is their canvas.',
            },
            {
                'icon': '🏡',
                'title': 'Warm Atmosphere',
                'description': 'Designed to feel like your favourite living room — comfortable seats, warm lighting, and the smell of fresh coffee in the air.',
            },
        ],
        'featured_items': [
            {
                'name': 'Signature Espresso',
                'category': 'Espresso',
                'description': 'Our house blend pulled to perfection — bold, rich, with a silky crema.',
                'price': '3.50',
                'image': 'https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=400&q=80',
            },
            {
                'name': 'Honey Oat Latte',
                'category': 'Latte',
                'description': 'Oat milk steamed to velvety perfection with a drizzle of wildflower honey.',
                'price': '5.50',
                'image': 'https://images.unsplash.com/photo-1561047029-3000c68339ca?w=400&q=80',
            },
            {
                'name': 'Avocado Toast',
                'category': 'Food',
                'description': 'Smashed avocado on sourdough with chili flakes, lemon, and microgreens.',
                'price': '9.00',
                'image': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c820?w=400&q=80',
            },
            {
                'name': 'Iced Pour Over',
                'category': 'Cold Brew',
                'description': 'Single-origin Ethiopian Yirgacheffe poured slow over ice. Naturally sweet.',
                'price': '6.00',
                'image': 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80',
            },
        ],
        'testimonials': [
            {
                'text': 'Brew & Bloom has become my daily ritual. The Honey Oat Latte is unlike anything I have ever tasted — it feels like a hug in a cup.',
                'name': 'Sarah Mitchell',
                'role': 'Regular Customer',
            },
            {
                'text': 'As a coffee snob, I am picky. This place actually gets it right. The single-origin pour overs are world-class. I will not go anywhere else.',
                'name': 'James Patel',
                'role': 'Coffee Enthusiast',
            },
            {
                'text': 'The atmosphere is perfect for working or catching up with friends. Friendly staff, beautiful space, and incredible food. Five stars always.',
                'name': 'Aisha Thompson',
                'role': 'Food Blogger',
            },
        ],
    }
    return render(request, 'home.html', context)


def menu(request):
    context = {
        'categories': [
            {'name': 'Espresso', 'slug': 'espresso', 'icon': '☕'},
            {'name': 'Cold Drinks', 'slug': 'cold', 'icon': '🧊'},
            {'name': 'Teas', 'slug': 'teas', 'icon': '🍵'},
            {'name': 'Food', 'slug': 'food', 'icon': '🥐'},
            {'name': 'Desserts', 'slug': 'desserts', 'icon': '🍰'},
        ],
        'menu_sections': [
            {
                'name': 'Espresso Drinks',
                'slug': 'espresso',
                'icon': '☕',
                'description': 'Classic and signature espresso-based beverages',
                'items': [
                    {
                        'name': 'Espresso',
                        'description': 'Double shot of our signature blend — rich, bold, perfectly balanced.',
                        'price': '3.50',
                        'badge': 'Classic',
                        'sizes': ['Single', 'Double', 'Triple'],
                        'image': 'https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=200&q=80',
                    },
                    {
                        'name': 'Flat White',
                        'description': 'Ristretto shots with silky micro-foamed whole milk.',
                        'price': '4.75',
                        'badge': '',
                        'sizes': ['Small', 'Regular'],
                        'image': 'https://images.unsplash.com/photo-1577961382953-f6b07d7d62e8?w=200&q=80',
                    },
                    {
                        'name': 'Honey Oat Latte',
                        'description': 'Oat milk, espresso, and a generous pour of wildflower honey.',
                        'price': '5.50',
                        'badge': 'Fan Fav',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1561047029-3000c68339ca?w=200&q=80',
                    },
                    {
                        'name': 'Lavender Cappuccino',
                        'description': 'House lavender syrup, espresso, and velvety steamed milk.',
                        'price': '5.25',
                        'badge': 'Seasonal',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1534778101976-62847782c213?w=200&q=80',
                    },
                    {
                        'name': 'Macchiato',
                        'description': 'Espresso marked with a touch of silky foam.',
                        'price': '4.00',
                        'badge': '',
                        'sizes': ['Single', 'Double'],
                        'image': 'https://images.unsplash.com/photo-1485808191679-5f86510bd9d4?w=200&q=80',
                    },
                    {
                        'name': 'Mocha',
                        'description': 'Espresso, dark chocolate, and steamed milk with whipped cream.',
                        'price': '5.75',
                        'badge': '',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=200&q=80',
                    },
                ],
            },
            {
                'name': 'Cold Drinks',
                'slug': 'cold',
                'icon': '🧊',
                'description': 'Refreshing cold brews and iced specialties',
                'items': [
                    {
                        'name': 'Iced Pour Over',
                        'description': 'Ethiopian Yirgacheffe brewed slow and poured over ice. Naturally sweet.',
                        'price': '6.00',
                        'badge': 'Best Seller',
                        'sizes': ['12oz', '16oz'],
                        'image': 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=200&q=80',
                    },
                    {
                        'name': 'Cold Brew',
                        'description': '18-hour steep in cold water. Smooth, low-acid, and intensely flavored.',
                        'price': '5.50',
                        'badge': '',
                        'sizes': ['12oz', '16oz', '24oz'],
                        'image': 'https://images.unsplash.com/photo-1566352781880-ac7bfe4f041e?w=200&q=80',
                    },
                    {
                        'name': 'Nitro Cold Brew',
                        'description': 'Cold brew infused with nitrogen for a creamy, Guinness-like texture.',
                        'price': '6.50',
                        'badge': 'Popular',
                        'sizes': ['12oz', '16oz'],
                        'image': 'https://images.unsplash.com/photo-1590301157890-4810ed352733?w=200&q=80',
                    },
                    {
                        'name': 'Iced Matcha Latte',
                        'description': 'Ceremonial grade matcha with oat milk and a hint of vanilla.',
                        'price': '5.50',
                        'badge': 'Vegan',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1515823662972-da6a2e4d3002?w=200&q=80',
                    },
                ],
            },
            {
                'name': 'Teas & More',
                'slug': 'teas',
                'icon': '🍵',
                'description': 'Hand-picked teas and wellness drinks',
                'items': [
                    {
                        'name': 'Chai Latte',
                        'description': 'House-spiced chai with steamed milk. Warming and aromatic.',
                        'price': '4.75',
                        'badge': '',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=200&q=80',
                    },
                    {
                        'name': 'Earl Grey',
                        'description': 'Loose leaf bergamot tea, served hot or iced with a lemon wheel.',
                        'price': '3.75',
                        'badge': '',
                        'sizes': ['Regular', 'Large'],
                        'image': 'https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=200&q=80',
                    },
                    {
                        'name': 'Golden Turmeric Latte',
                        'description': 'Oat milk, turmeric, ginger, black pepper, and a touch of honey.',
                        'price': '5.25',
                        'badge': 'Wellness',
                        'sizes': ['Regular'],
                        'image': 'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=200&q=80',
                    },
                ],
            },
            {
                'name': 'Food',
                'slug': 'food',
                'icon': '🥐',
                'description': 'Fresh pastries, toasts, and light bites',
                'items': [
                    {
                        'name': 'Butter Croissant',
                        'description': 'Flaky, golden, and buttery — baked fresh each morning.',
                        'price': '3.75',
                        'badge': 'Fresh Daily',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=200&q=80',
                    },
                    {
                        'name': 'Avocado Toast',
                        'description': 'Smashed avocado on sourdough with chili flakes, lemon, and microgreens.',
                        'price': '9.00',
                        'badge': '',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c820?w=200&q=80',
                    },
                    {
                        'name': 'Granola Bowl',
                        'description': 'House granola with Greek yogurt, seasonal berries, and honey.',
                        'price': '8.50',
                        'badge': 'Healthy',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1493770348161-369560ae357d?w=200&q=80',
                    },
                    {
                        'name': 'BLT Sandwich',
                        'description': 'Bacon, lettuce, tomato on toasted sourdough with herb aioli.',
                        'price': '11.00',
                        'badge': '',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=200&q=80',
                    },
                ],
            },
            {
                'name': 'Desserts',
                'slug': 'desserts',
                'icon': '🍰',
                'description': 'House-made sweets and baked treats',
                'items': [
                    {
                        'name': 'Banana Bread',
                        'description': 'Moist banana bread with walnuts and a brown sugar crust.',
                        'price': '4.25',
                        'badge': '',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1559703248-dcaaec9fab78?w=200&q=80',
                    },
                    {
                        'name': 'Tiramisu',
                        'description': 'Classic Italian dessert with espresso-soaked ladyfingers and mascarpone.',
                        'price': '6.50',
                        'badge': 'Chef Special',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=200&q=80',
                    },
                    {
                        'name': 'Chocolate Brownie',
                        'description': 'Dense, fudgy, and loaded with dark chocolate chips.',
                        'price': '4.75',
                        'badge': '',
                        'sizes': [],
                        'image': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=200&q=80',
                    },
                ],
            },
        ],
    }
    return render(request, 'menu.html', context)


def about(request):
    context = {
        'milestones': [
            {'year': '2012', 'title': 'The First Cup', 'description': 'Maria and James open Brew & Bloom with one espresso machine and a dream in Brooklyn.'},
            {'year': '2014', 'title': 'Roastery Opens', 'description': 'We begin roasting our own beans in-house, giving us full control over quality and flavour.'},
            {'year': '2016', 'title': 'Community Garden', 'description': 'We launch a rooftop herb garden, supplying fresh ingredients to our food menu year-round.'},
            {'year': '2018', 'title': 'Award-Winning Baristas', 'description': 'Head barista Leo Reyes wins the Northeast Regional Barista Championship.'},
            {'year': '2020', 'title': 'Online & Delivery', 'description': 'During the pandemic we pivot to online orders and bean subscriptions, reaching 1,000+ households.'},
            {'year': '2023', 'title': 'Expansion', 'description': 'We open our second location in Manhattan and launch a barista training academy.'},
        ],
        'team': [
            {
                'name': 'Maria Chen',
                'role': 'Co-Founder & CEO',
                'bio': 'Former pastry chef with 20 years of hospitality experience. Maria designed every inch of our space.',
                'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300&q=80',
            },
            {
                'name': 'James Chen',
                'role': 'Co-Founder & Head Roaster',
                'bio': 'Coffee scientist and origin traveler. James sources and roasts every single bean we serve.',
                'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&q=80',
            },
            {
                'name': 'Leo Reyes',
                'role': 'Head Barista',
                'bio': 'Regional barista champion. Leo trains our team and develops new seasonal espresso recipes.',
                'image': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&q=80',
            },
            {
                'name': 'Sophie Laurent',
                'role': 'Head of Food',
                'bio': 'Culinary school graduate turned café chef. Sophie crafts our food menu with local, seasonal ingredients.',
                'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&q=80',
            },
        ],
        'values': [
            {
                'icon': '🌍',
                'title': 'Sustainability',
                'description': 'We use compostable cups, source ethically, and donate 1% of revenue to reforestation projects.',
            },
            {
                'icon': '🤝',
                'title': 'Community',
                'description': 'Monthly events, local art exhibitions, and a space that belongs to the neighbourhood.',
            },
            {
                'icon': '✨',
                'title': 'Quality',
                'description': 'No shortcuts. From bean to cup, every step is deliberate and executed with care.',
            },
            {
                'icon': '❤️',
                'title': 'Inclusivity',
                'description': 'A welcoming space for everyone — with vegan, gluten-free, and nut-free options always available.',
            },
        ],
        'certifications': [
            'Fair Trade Certified',
            'USDA Organic',
            'Rainforest Alliance',
            'B Corp Member',
            'NYC Green Restaurant',
        ],
    }
    return render(request, 'about.html', context)


def contact(request):
    message_sent = False
    if request.method == 'POST':
        message_sent = True

    context = {
        'message_sent': message_sent,
        'faqs': [
            {
                'question': 'Do you accept walk-ins, or do I need a reservation?',
                'answer': 'We welcome walk-ins! Reservations are recommended for groups of 4 or more, especially on weekends.',
            },
            {
                'question': 'Do you have dairy-free or vegan options?',
                'answer': 'Absolutely. We offer oat, almond, soy, and coconut milk alternatives. Most of our food menu has vegan options too.',
            },
            {
                'question': 'Can I host private events at Brew & Bloom?',
                'answer': 'Yes! We offer private bookings for birthdays, corporate events, and pop-ups. Contact us for details and availability.',
            },
            {
                'question': 'Do you sell your coffee beans to take home?',
                'answer': 'We sell our roasted beans in 250g and 1kg bags. We also offer a monthly subscription — ask at the counter or contact us online.',
            },
            {
                'question': 'Is there parking nearby?',
                'answer': 'Street parking is available on Maple Ave. There is also a public garage one block away on 5th Street.',
            },
        ],
    }
    return render(request, 'contact.html', context)
