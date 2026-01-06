import type { Restaurant } from '../types';

export const mockRestaurants: Restaurant[] = [
    {
        id: '1',
        name: 'Sate Khas Senayan',
        description: 'Menyajikan sate dan masakan khas Jawa dengan cita rasa otentik sejak 1974.',
        cuisine: 'Indonesian',
        location: 'Jakarta Pusat',
        address: 'Jl. Kebon Sirih No. 31A, Jakarta Pusat',
        phone: '+62 21 3192 6238',
        email: 'info@satekhassenayan.com',
        priceRange: 'moderate',
        rating: 4.7,
        reviewCount: 1250,
        images: [
            'https://images.unsplash.com/photo-1555126634-323283e090fa?w=800',
            'https://images.unsplash.com/photo-1529563021893-cc83c992d759?w=800',
            'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800',
        ],
        openingHours: {
            monday: { open: '10:00', close: '22:00' },
            tuesday: { open: '10:00', close: '22:00' },
            wednesday: { open: '10:00', close: '22:00' },
            thursday: { open: '10:00', close: '22:00' },
            friday: { open: '10:00', close: '22:00' },
            saturday: { open: '10:00', close: '22:00' },
            sunday: { open: '10:00', close: '22:00' },
        },
        features: ['WiFi', 'Air Conditioning', 'Family Friendly', 'Halal'],
        capacity: 120,
        menu: [
            {
                id: 'm1-1',
                name: 'Sate Ayam Bumbu Blora',
                description: 'Sate ayam juicy dengan bumbu kacang halus yang gurih.',
                price: 72000,
                image: 'https://images.unsplash.com/photo-1630303866167-9c6061c0d4a9?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm1-2',
                name: 'Tahu Telur',
                description: 'Tahu goreng telur disajikan dengan toge dan saus petis.',
                price: 48000,
                image: 'https://images.unsplash.com/photo-1565257969871-70cb07153a9e?w=800', // Ilustrasi Tahu
                category: 'Food',
                isBestSeller: false
            },
            {
                id: 'm1-3',
                name: 'Es Cendol Durian',
                description: 'Minuman segar santan gula merah dengan topping durian asli.',
                price: 35000,
                image: 'https://images.unsplash.com/photo-1563729760305-65a88e7d2301?w=800', // Ilustrasi Dessert
                category: 'Drink',
                isBestSeller: true
            }
        ]
    },
    {
        id: '2',
        name: 'Bebek Tepi Sawah',
        description: 'Restoran ikonik dari Bali yang menyajikan Bebek Goreng Crispy.',
        cuisine: 'Balinese',
        location: 'Ubud, Bali',
        address: 'Jl. Raya Goa Gajah, Br. Teges Peliatan, Ubud',
        phone: '+62 361 975656',
        email: 'ubud@bebektepisawah.com',
        priceRange: 'moderate',
        rating: 4.8,
        reviewCount: 2340,
        images: [
            'https://images.unsplash.com/photo-1604423043492-41303788de80?w=800',
            'https://images.unsplash.com/photo-1563897539633-7374c276c212?w=800',
            'https://images.unsplash.com/photo-1533630667089-8742b8277258?w=800',
        ],
        openingHours: {
            monday: { open: '10:00', close: '22:00' },
            tuesday: { open: '10:00', close: '22:00' },
            wednesday: { open: '10:00', close: '22:00' },
            thursday: { open: '10:00', close: '22:00' },
            friday: { open: '10:00', close: '22:00' },
            saturday: { open: '10:00', close: '22:00' },
            sunday: { open: '10:00', close: '22:00' },
        },
        features: ['Outdoor Seating', 'Rice Field View', 'Traditional Music', 'Souvenir Shop'],
        capacity: 200,
        menu: [
            {
                id: 'm2-1',
                name: 'Tepi Sawah Crispy Duck',
                description: 'Bebek goreng garing setengah ekor dengan 3 jenis sambal bali.',
                price: 135000,
                image: 'https://images.unsplash.com/photo-1628269728448-735165427d11?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm2-2',
                name: 'Ayam Betutu',
                description: 'Ayam dimasak dengan bumbu rempah bali yang kaya rasa.',
                price: 95000,
                image: 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm2-3',
                name: 'Fresh Coconut',
                description: 'Kelapa muda utuh yang segar.',
                price: 35000,
                image: 'https://images.unsplash.com/photo-1621356778940-d9d300755919?w=800',
                category: 'Drink',
                isBestSeller: false
            }
        ]
    },
    {
        id: '3',
        name: 'Padang Merdeka',
        description: 'Menyajikan masakan Padang premium dengan konsep modern.',
        cuisine: 'Padang',
        location: 'Kota Tua',
        address: 'Jl. Lada No. 1, Pinangsia, Tamansari, Jakarta Barat',
        phone: '+62 21 691 9813',
        email: 'info@padangmerdeka.com',
        priceRange: 'moderate',
        rating: 4.6,
        reviewCount: 1580,
        images: [
            'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800',
            'https://images.unsplash.com/photo-1606471191009-63994c53433b?w=800',
            'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800',
        ],
        openingHours: {
            monday: { open: '09:00', close: '21:00' },
            tuesday: { open: '09:00', close: '21:00' },
            wednesday: { open: '09:00', close: '21:00' },
            thursday: { open: '09:00', close: '21:00' },
            friday: { open: '09:00', close: '21:00' },
            saturday: { open: '09:00', close: '22:00' },
            sunday: { open: '09:00', close: '22:00' },
        },
        features: ['VIP Room', 'Buffet Style', 'Instagrammable', 'Strategic Location'],
        capacity: 150,
        menu: [
            {
                id: 'm3-1',
                name: 'Rendang Sapi',
                description: 'Daging sapi yang dimasak perlahan dengan santan dan rempah.',
                price: 28000,
                image: 'https://images.unsplash.com/photo-1603083561504-20456102f4f2?w=800', // Ilustrasi Rendang
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm3-2',
                name: 'Ayam Pop',
                description: 'Ayam goreng putih khas Padang dengan sambal merah.',
                price: 26000,
                image: 'https://images.unsplash.com/photo-1569058242252-6235b7e289c8?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm3-3',
                name: 'Jus Alpukat',
                description: 'Jus alpukat kental dengan susu cokelat.',
                price: 32000,
                image: 'https://images.unsplash.com/photo-1603569283847-aa295f0d016a?w=800',
                category: 'Drink',
                isBestSeller: false
            }
        ]
    },
    {
        id: '4',
        name: 'Lara Djonggrang',
        description: 'Restoran mewah yang menggabungkan sejarah, seni, dan kuliner Nusantara.',
        cuisine: 'Indonesian',
        location: 'Menteng',
        address: 'Jl. Teuku Cik Ditiro No. 4, Menteng, Jakarta Pusat',
        phone: '+62 21 315 3252',
        email: 'laradjonggrang@tuguhotels.com',
        priceRange: 'fine-dining',
        rating: 4.9,
        reviewCount: 890,
        images: [
            'https://images.unsplash.com/photo-1578474843222-27f122946c6f?w=800',
            'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=800',
            'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800',
        ],
        openingHours: {
            monday: { open: '11:00', close: '23:00' },
            tuesday: { open: '11:00', close: '23:00' },
            wednesday: { open: '11:00', close: '23:00' },
            thursday: { open: '11:00', close: '23:00' },
            friday: { open: '11:00', close: '00:00' },
            saturday: { open: '11:00', close: '00:00' },
            sunday: { open: '11:00', close: '23:00' },
        },
        features: ['Fine Dining', 'Historical Building', 'Art Gallery', 'Romantic Ambiance'],
        capacity: 100,
        menu: [
            {
                id: 'm4-1',
                name: 'Pasar Sate',
                description: 'Aneka sate nusantara disajikan di atas kapal kayu.',
                price: 185000,
                image: 'https://images.unsplash.com/photo-1533758362483-e5743a139943?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm4-2',
                name: 'Nasi Goreng Djonggrang',
                description: 'Nasi goreng signature dengan penyajian tumpeng mini.',
                price: 110000,
                image: 'https://images.unsplash.com/photo-1603133872878-684f571d70f2?w=800',
                category: 'Food',
                isBestSeller: false
            },
            {
                id: 'm4-3',
                name: 'Es Campur Mahameru',
                description: 'Es campur tradisional dengan sirup spesial.',
                price: 55000,
                image: 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800', // Ilustrasi Es
                category: 'Dessert',
                isBestSeller: true
            }
        ]
    },
    {
        id: '5',
        name: 'Plataran Dharmawangsa',
        description: 'Hunian bangsawan Jawa yang diubah menjadi restoran mewah.',
        cuisine: 'Indonesian',
        location: 'Kebayoran Baru',
        address: 'Jl. Dharmawangsa Raya No. 6, Kebayoran Baru',
        phone: '+62 21 290 44167',
        email: 'reservation.dharmawangsa@plataran.com',
        priceRange: 'fine-dining',
        rating: 4.8,
        reviewCount: 760,
        images: [
            'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800',
            'https://images.unsplash.com/photo-1575424909138-7074f3f3de92?w=800',
            'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800',
        ],
        openingHours: {
            monday: { open: '11:00', close: '22:00' },
            tuesday: { open: '11:00', close: '22:00' },
            wednesday: { open: '11:00', close: '22:00' },
            thursday: { open: '11:00', close: '22:00' },
            friday: { open: '11:00', close: '23:00' },
            saturday: { open: '11:00', close: '23:00' },
            sunday: { open: '11:00', close: '22:00' },
        },
        features: ['Javanese Joglo', 'Private Dining', 'Valet Parking', 'Wedding Venue'],
        capacity: 150,
        menu: [
            {
                id: 'm5-1',
                name: 'Dendeng Batokok',
                description: 'Daging sapi kering renyah dengan sambal lado hijau.',
                price: 165000,
                image: 'https://images.unsplash.com/photo-1628108985172-e56580f4f9f7?w=800', // Ilustrasi Daging
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm5-2',
                name: 'Kerapu Tim Malas',
                description: 'Ikan kerapu segar ditim dengan jahe dan kecap asin.',
                price: 245000,
                image: 'https://images.unsplash.com/photo-1599577741366-b3e34b41913c?w=800',
                category: 'Food',
                isBestSeller: false
            },
            {
                id: 'm5-3',
                name: 'Wedang Ronde',
                description: 'Minuman jahe hangat dengan bola-bola ketan isi kacang.',
                price: 45000,
                image: 'https://images.unsplash.com/photo-1626129482570-55d8d0115c4d?w=800', // Ilustrasi Tradisional Drink
                category: 'Drink',
                isBestSeller: true
            }
        ]
    },
    {
        id: '6',
        name: 'Ikan Bakar Cianjur',
        description: 'Spesialis hidangan Sunda dengan Gurame Bakar yang legendaris.',
        cuisine: 'Sundanese',
        location: 'Surabaya',
        address: 'Jl. Sulawesi No. 54, Gubeng, Surabaya',
        phone: '+62 31 503 1333',
        email: 'info@ibc.id',
        priceRange: 'moderate',
        rating: 4.5,
        reviewCount: 3200,
        images: [
            'https://images.unsplash.com/photo-1535400255456-984241443b29?w=800',
            'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800',
            'https://images.unsplash.com/photo-1544025162-d76690b67f61?w=800',
        ],
        openingHours: {
            monday: { open: '10:00', close: '22:00' },
            tuesday: { open: '10:00', close: '22:00' },
            wednesday: { open: '10:00', close: '22:00' },
            thursday: { open: '10:00', close: '22:00' },
            friday: { open: '10:00', close: '22:00' },
            saturday: { open: '10:00', close: '22:00' },
            sunday: { open: '10:00', close: '22:00' },
        },
        features: ['Family Friendly', 'Large Capacity', 'Takeaway', 'Prayer Room'],
        capacity: 300,
        menu: [
            {
                id: 'm6-1',
                name: 'Gurame Bakar',
                description: 'Ikan gurame dibakar dengan bumbu manis gurih khas Cianjur.',
                price: 98000,
                image: 'https://images.unsplash.com/photo-1580456108502-866418d184f4?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm6-2',
                name: 'Nasi Liwet',
                description: 'Nasi gurih dimasak dalam panci kastrol dengan ikan teri.',
                price: 45000,
                image: 'https://images.unsplash.com/photo-1634626132717-38df374d284e?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm6-3',
                name: 'Tumis Kangkung Terasi',
                description: 'Sayuran kangkung segar ditumis dengan terasi harum.',
                price: 28000,
                image: 'https://images.unsplash.com/photo-1563294320-f47225bd04ac?w=800',
                category: 'Food',
                isBestSeller: false
            }
        ]
    },
    {
        id: '7',
        name: 'Seribu Rasa',
        description: 'Cita rasa kuliner Asia Tenggara dan Indonesia yang dikemas dalam nuansa elegan.',
        cuisine: 'Southeast Asian',
        location: 'Menteng, Jakarta',
        address: 'Jl. H. Agus Salim No. 128, Menteng, Jakarta Pusat',
        phone: '+62 21 392 8892',
        email: 'menteng@seriburasa.com',
        priceRange: 'expensive',
        rating: 4.8,
        reviewCount: 1800,
        images: [
            'https://images.unsplash.com/photo-1514361892635-6b07e31e75f9?w=800',
            'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800',
            'https://images.unsplash.com/photo-1581349485608-9469926a8e5e?w=800',
        ],
        openingHours: {
            monday: { open: '11:00', close: '22:00' },
            tuesday: { open: '11:00', close: '22:00' },
            wednesday: { open: '11:00', close: '22:00' },
            thursday: { open: '11:00', close: '22:00' },
            friday: { open: '11:00', close: '22:00' },
            saturday: { open: '11:00', close: '22:00' },
            sunday: { open: '11:00', close: '22:00' },
        },
        features: ['Private Room', 'Bar', 'Seafood Specialist', 'Business Dining'],
        capacity: 200,
        menu: [
            {
                id: 'm7-1',
                name: 'Gulai Kepala Ikan',
                description: 'Kepala ikan kakap dimasak dalam kuah gulai kental.',
                price: 180000,
                image: 'https://images.unsplash.com/photo-1614984288414-b1eb217e17cb?w=800', // Ilustrasi Curry
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm7-2',
                name: 'Black Pepper Crab',
                description: 'Kepiting segar dimasak dengan saus lada hitam pedas.',
                price: 250000,
                image: 'https://images.unsplash.com/photo-1585250954930-58f707f1d467?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm7-3',
                name: 'Thai Mango Salad',
                description: 'Salad mangga muda dengan dressing asam pedas segar.',
                price: 65000,
                image: 'https://images.unsplash.com/photo-1506459345638-765ed9f31525?w=800',
                category: 'Food',
                isBestSeller: false
            }
        ]
    },
    {
        id: '8',
        name: 'Gudeg Yu Djum',
        description: 'Legenda kuliner Yogyakarta sejak 1951. Gudeg kering dengan rasa manis gurih.',
        cuisine: 'Javanese',
        location: 'Yogyakarta',
        address: 'Jl. Wijilan No. 167, Panembahan, Yogyakarta',
        phone: '+62 274 370 381',
        email: 'info@gudegyudjum.com',
        priceRange: 'cheap',
        rating: 4.6,
        reviewCount: 4500,
        images: [
            'https://images.unsplash.com/photo-1626202133285-f37dd782415c?w=800',
            'https://images.unsplash.com/photo-1505253668822-420429a3d4be?w=800',
            'https://images.unsplash.com/photo-1568271714652-5a2139bc62c1?w=800',
        ],
        openingHours: {
            monday: { open: '06:00', close: '22:00' },
            tuesday: { open: '06:00', close: '22:00' },
            wednesday: { open: '06:00', close: '22:00' },
            thursday: { open: '06:00', close: '22:00' },
            friday: { open: '06:00', close: '22:00' },
            saturday: { open: '06:00', close: '22:00' },
            sunday: { open: '06:00', close: '22:00' },
        },
        features: ['Legendary', 'Souvenir', 'Traditional', 'Fast Service'],
        capacity: 80,
        menu: [
            {
                id: 'm8-1',
                name: 'Nasi Gudeg Komplit',
                description: 'Nasi dengan gudeg, krecek, telur, dan suwir ayam.',
                price: 45000,
                image: 'https://images.unsplash.com/photo-1626202133285-f37dd782415c?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm8-2',
                name: 'Ayam Opor Bagian Paha',
                description: 'Ayam opor bumbu kuning yang empuk.',
                price: 35000,
                image: 'https://images.unsplash.com/photo-1603083561556-9e8a735392bd?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm8-3',
                name: 'Teh Poci Gula Batu',
                description: 'Teh wangi melati disajikan di poci tanah liat.',
                price: 15000,
                image: 'https://images.unsplash.com/photo-1564770178496-51e442971206?w=800',
                category: 'Drink',
                isBestSeller: false
            }
        ]
    },
    {
        id: '9',
        name: 'Bandar Djakarta',
        description: 'Pasar ikan segar di pinggir laut. Pilih sendiri ikan, udang, kepiting hidup.',
        cuisine: 'Seafood',
        location: 'Ancol, Jakarta',
        address: 'Pintu Timur Taman Impian Jaya Ancol, Jakarta Utara',
        phone: '+62 21 645 5472',
        email: 'reservation@bandar-djakarta.com',
        priceRange: 'moderate',
        rating: 4.5,
        reviewCount: 5100,
        images: [
            'https://images.unsplash.com/photo-1553184620-3b28b5c1cb2d?w=800',
            'https://images.unsplash.com/photo-1621348122709-0d322b649d28?w=800',
            'https://images.unsplash.com/photo-1596627685789-53b925b42605?w=800',
        ],
        openingHours: {
            monday: { open: '11:00', close: '23:00' },
            tuesday: { open: '11:00', close: '23:00' },
            wednesday: { open: '11:00', close: '23:00' },
            thursday: { open: '11:00', close: '23:00' },
            friday: { open: '11:00', close: '23:30' },
            saturday: { open: '10:00', close: '23:30' },
            sunday: { open: '10:00', close: '23:00' },
        },
        features: ['Live Seafood', 'Ocean View', 'Outdoor Seating', 'Live Music'],
        capacity: 500,
        menu: [
            {
                id: 'm9-1',
                name: 'Kepiting Saus Padang',
                description: 'Kepiting hidup dimasak dengan saus padang yang pedas nendang.',
                price: 320000,
                image: 'https://images.unsplash.com/photo-1553184620-3b28b5c1cb2d?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm9-2',
                name: 'Udang Peci Bakar Madu',
                description: 'Udang bakar dengan olesan madu dan lemon.',
                price: 150000,
                image: 'https://images.unsplash.com/photo-1606132646638-3f5af769974c?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm9-3',
                name: 'Cumi Goreng Tepung',
                description: 'Cumi ring digoreng renyah dengan saus tartar.',
                price: 85000,
                image: 'https://images.unsplash.com/photo-1605493666373-162d142d7637?w=800',
                category: 'Food',
                isBestSeller: false
            }
        ]
    },
    {
        id: '10',
        name: 'Kampung Daun',
        description: 'Menikmati hidangan Sunda di dalam saung privat di lembah hutan.',
        cuisine: 'Sundanese',
        location: 'Bandung',
        address: 'Jl. Sersan Bajuri No. 88, Cihideung, Bandung',
        phone: '+62 22 278 7915',
        email: 'info@kampungdaun.id',
        priceRange: 'moderate',
        rating: 4.7,
        reviewCount: 3800,
        images: [
            'https://images.unsplash.com/photo-1445964047600-cdbdb873673d?w=800',
            'https://images.unsplash.com/photo-1625937759425-63402e86d009?w=800',
            'https://images.unsplash.com/photo-1605333190886-5d63be538466?w=800',
        ],
        openingHours: {
            monday: { open: '10:00', close: '22:00' },
            tuesday: { open: '10:00', close: '22:00' },
            wednesday: { open: '10:00', close: '22:00' },
            thursday: { open: '10:00', close: '22:00' },
            friday: { open: '10:00', close: '23:00' },
            saturday: { open: '09:00', close: '23:00' },
            sunday: { open: '09:00', close: '22:00' },
        },
        features: ['Nature View', 'Private Saung', 'Romantic', 'Cool Climate'],
        capacity: 400,
        menu: [
            {
                id: 'm10-1',
                name: 'Nasi Timbel Komplit',
                description: 'Nasi bungkus daun pisang, ayam goreng, tahu tempe, sambal.',
                price: 65000,
                image: 'https://images.unsplash.com/photo-1629854445391-7d4d03d3c809?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm10-2',
                name: 'Surabi Durian',
                description: 'Pancake tradisional Bandung dengan saus durian.',
                price: 30000,
                image: 'https://images.unsplash.com/photo-1598214886806-c87b84b7078b?w=800', // Ilustrasi Pancake
                category: 'Dessert',
                isBestSeller: true
            },
            {
                id: 'm10-3',
                name: 'Bajigur',
                description: 'Minuman santan hangat dengan gula aren dan jahe.',
                price: 25000,
                image: 'https://images.unsplash.com/photo-1588661730030-a355606d2890?w=800',
                category: 'Drink',
                isBestSeller: false
            }
        ]
    },
    {
        id: '11',
        name: 'Merah Putih',
        description: 'Eksperimen masakan Indonesia klasik dan modern di bangunan megah.',
        cuisine: 'Modern Indonesian',
        location: 'Seminyak, Bali',
        address: 'Jl. Petitenget No. 100X, Kerobokan, Bali',
        phone: '+62 361 8465950',
        email: 'info@merahputihbali.com',
        priceRange: 'expensive',
        rating: 4.9,
        reviewCount: 2100,
        images: [
            'https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800',
            'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800',
            'https://images.unsplash.com/photo-1544148103-0773bf10d330?w=800',
        ],
        openingHours: {
            monday: { open: '12:00', close: '00:00' },
            tuesday: { open: '12:00', close: '00:00' },
            wednesday: { open: '12:00', close: '00:00' },
            thursday: { open: '12:00', close: '00:00' },
            friday: { open: '12:00', close: '00:00' },
            saturday: { open: '12:00', close: '00:00' },
            sunday: { open: '12:00', close: '00:00' },
        },
        features: ['Architecture', 'Cocktail Bar', 'Vegetarian Options', 'Valet'],
        capacity: 180,
        menu: [
            {
                id: 'm11-1',
                name: 'Babi Guling',
                description: 'Suckling pig khas Bali dengan kulit renyah.',
                price: 220000,
                image: 'https://images.unsplash.com/photo-1628108985172-e56580f4f9f7?w=800', // Ilustrasi Roast Pork
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm11-2',
                name: 'Soft Shell Crab',
                description: 'Kepiting soka goreng dengan bumbu rujak.',
                price: 145000,
                image: 'https://images.unsplash.com/photo-1551608756-324df39c43d8?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm11-3',
                name: 'Bali Martini',
                description: 'Cocktail khas dengan arak Bali dan buah tropis.',
                price: 120000,
                image: 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800',
                category: 'Drink',
                isBestSeller: false
            }
        ]
    },
    {
        id: '12',
        name: 'Sarang Oci',
        description: 'Cita rasa asli Manado yang pedas dan segar.',
        cuisine: 'Manadonese',
        location: 'Jakarta Selatan',
        address: 'Jl. Bulungan No. 22, Blok M, Jakarta Selatan',
        phone: '+62 21 722 0000',
        email: 'info@sarangoci.com',
        priceRange: 'moderate',
        rating: 4.6,
        reviewCount: 1400,
        images: [
            'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800',
            'https://images.unsplash.com/photo-1615937657715-bc7b4b7962c1?w=800',
            'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800',
        ],
        openingHours: {
            monday: { open: '10:00', close: '21:30' },
            tuesday: { open: '10:00', close: '21:30' },
            wednesday: { open: '10:00', close: '21:30' },
            thursday: { open: '10:00', close: '21:30' },
            friday: { open: '10:00', close: '22:00' },
            saturday: { open: '10:00', close: '22:00' },
            sunday: { open: '10:00', close: '21:30' },
        },
        features: ['Spicy Food', 'Halal', 'Family Dining', 'Authentic Taste'],
        capacity: 90,
        menu: [
            {
                id: 'm12-1',
                name: 'Ekor Tenggiri Bakar',
                description: 'Ekor ikan tenggiri dibakar dengan bumbu rica.',
                price: 95000,
                image: 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm12-2',
                name: 'Perkedel Jagung',
                description: 'Gorengan jagung manis yang super renyah.',
                price: 35000,
                image: 'https://images.unsplash.com/photo-1615937657715-bc7b4b7962c1?w=800',
                category: 'Food',
                isBestSeller: true
            },
            {
                id: 'm12-3',
                name: 'Es Brenebon',
                description: 'Es kacang merah khas Manado dengan susu cokelat.',
                price: 30000,
                image: 'https://images.unsplash.com/photo-1550614000-4b9519e072eb?w=800', // Ilustrasi Es
                category: 'Dessert',
                isBestSeller: false
            }
        ]
    },
];

export const generateTimeSlots = (date: string): string[] => {
    const slots = [];
    for (let hour = 11; hour <= 21; hour++) {
        slots.push(`${hour.toString().padStart(2, '0')}:00`);
        if (hour < 21) {
            slots.push(`${hour.toString().padStart(2, '0')}:30`);
        }
    }
    return slots;
};