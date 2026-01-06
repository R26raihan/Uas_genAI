-- Database Seed Script for RAG Resto
-- Generated from src/data/mockData.ts

-- 1. Create Tables
CREATE TABLE IF NOT EXISTS restaurants (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    cuisine VARCHAR(100),
    location VARCHAR(100),
    address TEXT,
    phone VARCHAR(50),
    email VARCHAR(100),
    price_range VARCHAR(50),
    rating DECIMAL(3, 2),
    review_count INT,
    capacity INT
);

CREATE TABLE IF NOT EXISTS restaurant_images (
    id SERIAL PRIMARY KEY,
    restaurant_id VARCHAR(50) REFERENCES restaurants(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS opening_hours (
    id SERIAL PRIMARY KEY,
    restaurant_id VARCHAR(50) REFERENCES restaurants(id) ON DELETE CASCADE,
    day_of_week VARCHAR(15) NOT NULL,
    open_time VARCHAR(10),
    close_time VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS restaurant_features (
    id SERIAL PRIMARY KEY,
    restaurant_id VARCHAR(50) REFERENCES restaurants(id) ON DELETE CASCADE,
    feature VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS menu_items (
    id VARCHAR(50) PRIMARY KEY,
    restaurant_id VARCHAR(50) REFERENCES restaurants(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price INT,
    image_url TEXT,
    category VARCHAR(100),
    is_best_seller BOOLEAN DEFAULT FALSE
);

-- 2. Insert Data
-- IDs: '1' - '12'

-- Sate Khas Senayan (1)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('1', 'Sate Khas Senayan', 'Menyajikan sate dan masakan khas Jawa dengan cita rasa otentik sejak 1974.', 'Indonesian', 'Jakarta Pusat', 'Jl. Kebon Sirih No. 31A, Jakarta Pusat', '+62 21 3192 6238', 'info@satekhassenayan.com', 'moderate', 4.7, 1250, 120);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('1', 'https://images.unsplash.com/photo-1555126634-323283e090fa?w=800');
INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('1', 'https://images.unsplash.com/photo-1529563021893-cc83c992d759?w=800');
INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('1', 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'monday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'tuesday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'wednesday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'thursday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'friday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'saturday', '10:00', '22:00');
INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('1', 'sunday', '10:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('1', 'WiFi'), ('1', 'Air Conditioning'), ('1', 'Family Friendly'), ('1', 'Halal');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m1-1', '1', 'Sate Ayam Bumbu Blora', 'Sate ayam juicy dengan bumbu kacang halus yang gurih.', 72000, 'https://images.unsplash.com/photo-1630303866167-9c6061c0d4a9?w=800', 'Food', true),
('m1-2', '1', 'Tahu Telur', 'Tahu goreng telur disajikan dengan toge dan saus petis.', 48000, 'https://images.unsplash.com/photo-1565257969871-70cb07153a9e?w=800', 'Food', false),
('m1-3', '1', 'Es Cendol Durian', 'Minuman segar santan gula merah dengan topping durian asli.', 35000, 'https://images.unsplash.com/photo-1563729760305-65a88e7d2301?w=800', 'Drink', true);

-- Bebek Tepi Sawah (2)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('2', 'Bebek Tepi Sawah', 'Restoran ikonik dari Bali yang menyajikan Bebek Goreng Crispy.', 'Balinese', 'Ubud, Bali', 'Jl. Raya Goa Gajah, Br. Teges Peliatan, Ubud', '+62 361 975656', 'ubud@bebektepisawah.com', 'moderate', 4.8, 2340, 200);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('2', 'https://images.unsplash.com/photo-1604423043492-41303788de80?w=800');
INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('2', 'https://images.unsplash.com/photo-1563897539633-7374c276c212?w=800');
INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('2', 'https://images.unsplash.com/photo-1533630667089-8742b8277258?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('2', 'monday', '10:00', '22:00'), ('2', 'tuesday', '10:00', '22:00'), ('2', 'wednesday', '10:00', '22:00'), ('2', 'thursday', '10:00', '22:00'), ('2', 'friday', '10:00', '22:00'), ('2', 'saturday', '10:00', '22:00'), ('2', 'sunday', '10:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('2', 'Outdoor Seating'), ('2', 'Rice Field View'), ('2', 'Traditional Music'), ('2', 'Souvenir Shop');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m2-1', '2', 'Tepi Sawah Crispy Duck', 'Bebek goreng garing setengah ekor dengan 3 jenis sambal bali.', 135000, 'https://images.unsplash.com/photo-1628269728448-735165427d11?w=800', 'Food', true),
('m2-2', '2', 'Ayam Betutu', 'Ayam dimasak dengan bumbu rempah bali yang kaya rasa.', 95000, 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?w=800', 'Food', true),
('m2-3', '2', 'Fresh Coconut', 'Kelapa muda utuh yang segar.', 35000, 'https://images.unsplash.com/photo-1621356778940-d9d300755919?w=800', 'Drink', false);

-- Padang Merdeka (3)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('3', 'Padang Merdeka', 'Menyajikan masakan Padang premium dengan konsep modern.', 'Padang', 'Kota Tua', 'Jl. Lada No. 1, Pinangsia, Tamansari, Jakarta Barat', '+62 21 691 9813', 'info@padangmerdeka.com', 'moderate', 4.6, 1580, 150);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('3', 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800'), ('3', 'https://images.unsplash.com/photo-1606471191009-63994c53433b?w=800'), ('3', 'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('3', 'monday', '09:00', '21:00'), ('3', 'tuesday', '09:00', '21:00'), ('3', 'wednesday', '09:00', '21:00'), ('3', 'thursday', '09:00', '21:00'), ('3', 'friday', '09:00', '21:00'), ('3', 'saturday', '09:00', '22:00'), ('3', 'sunday', '09:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('3', 'VIP Room'), ('3', 'Buffet Style'), ('3', 'Instagrammable'), ('3', 'Strategic Location');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m3-1', '3', 'Rendang Sapi', 'Daging sapi yang dimasak perlahan dengan santan dan rempah.', 28000, 'https://images.unsplash.com/photo-1603083561504-20456102f4f2?w=800', 'Food', true),
('m3-2', '3', 'Ayam Pop', 'Ayam goreng putih khas Padang dengan sambal merah.', 26000, 'https://images.unsplash.com/photo-1569058242252-6235b7e289c8?w=800', 'Food', true),
('m3-3', '3', 'Jus Alpukat', 'Jus alpukat kental dengan susu cokelat.', 32000, 'https://images.unsplash.com/photo-1603569283847-aa295f0d016a?w=800', 'Drink', false);

-- Lara Djonggrang (4)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('4', 'Lara Djonggrang', 'Restoran mewah yang menggabungkan sejarah, seni, dan kuliner Nusantara.', 'Indonesian', 'Menteng', 'Jl. Teuku Cik Ditiro No. 4, Menteng, Jakarta Pusat', '+62 21 315 3252', 'laradjonggrang@tuguhotels.com', 'fine-dining', 4.9, 890, 100);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('4', 'https://images.unsplash.com/photo-1578474843222-27f122946c6f?w=800'), ('4', 'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=800'), ('4', 'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('4', 'monday', '11:00', '23:00'), ('4', 'tuesday', '11:00', '23:00'), ('4', 'wednesday', '11:00', '23:00'), ('4', 'thursday', '11:00', '23:00'), ('4', 'friday', '11:00', '00:00'), ('4', 'saturday', '11:00', '00:00'), ('4', 'sunday', '11:00', '23:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('4', 'Fine Dining'), ('4', 'Historical Building'), ('4', 'Art Gallery'), ('4', 'Romantic Ambiance');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m4-1', '4', 'Pasar Sate', 'Aneka sate nusantara disajikan di atas kapal kayu.', 185000, 'https://images.unsplash.com/photo-1533758362483-e5743a139943?w=800', 'Food', true),
('m4-2', '4', 'Nasi Goreng Djonggrang', 'Nasi goreng signature dengan penyajian tumpeng mini.', 110000, 'https://images.unsplash.com/photo-1603133872878-684f571d70f2?w=800', 'Food', false),
('m4-3', '4', 'Es Campur Mahameru', 'Es campur tradisional dengan sirup spesial.', 55000, 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800', 'Dessert', true);

-- Plataran Dharmawangsa (5)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('5', 'Plataran Dharmawangsa', 'Hunian bangsawan Jawa yang diubah menjadi restoran mewah.', 'Indonesian', 'Kebayoran Baru', 'Jl. Dharmawangsa Raya No. 6, Kebayoran Baru', '+62 21 290 44167', 'reservation.dharmawangsa@plataran.com', 'fine-dining', 4.8, 760, 150);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('5', 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800'), ('5', 'https://images.unsplash.com/photo-1575424909138-7074f3f3de92?w=800'), ('5', 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('5', 'monday', '11:00', '22:00'), ('5', 'tuesday', '11:00', '22:00'), ('5', 'wednesday', '11:00', '22:00'), ('5', 'thursday', '11:00', '22:00'), ('5', 'friday', '11:00', '23:00'), ('5', 'saturday', '11:00', '23:00'), ('5', 'sunday', '11:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('5', 'Javanese Joglo'), ('5', 'Private Dining'), ('5', 'Valet Parking'), ('5', 'Wedding Venue');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m5-1', '5', 'Dendeng Batokok', 'Daging sapi kering renyah dengan sambal lado hijau.', 165000, 'https://images.unsplash.com/photo-1628108985172-e56580f4f9f7?w=800', 'Food', true),
('m5-2', '5', 'Kerapu Tim Malas', 'Ikan kerapu segar ditim dengan jahe dan kecap asin.', 245000, 'https://images.unsplash.com/photo-1599577741366-b3e34b41913c?w=800', 'Food', false),
('m5-3', '5', 'Wedang Ronde', 'Minuman jahe hangat dengan bola-bola ketan isi kacang.', 45000, 'https://images.unsplash.com/photo-1626129482570-55d8d0115c4d?w=800', 'Drink', true);

-- Ikan Bakar Cianjur (6)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('6', 'Ikan Bakar Cianjur', 'Spesialis hidangan Sunda dengan Gurame Bakar yang legendaris.', 'Sundanese', 'Surabaya', 'Jl. Sulawesi No. 54, Gubeng, Surabaya', '+62 31 503 1333', 'info@ibc.id', 'moderate', 4.5, 3200, 300);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('6', 'https://images.unsplash.com/photo-1535400255456-984241443b29?w=800'), ('6', 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800'), ('6', 'https://images.unsplash.com/photo-1544025162-d76690b67f61?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('6', 'monday', '10:00', '22:00'), ('6', 'tuesday', '10:00', '22:00'), ('6', 'wednesday', '10:00', '22:00'), ('6', 'thursday', '10:00', '22:00'), ('6', 'friday', '10:00', '22:00'), ('6', 'saturday', '10:00', '22:00'), ('6', 'sunday', '10:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('6', 'Family Friendly'), ('6', 'Large Capacity'), ('6', 'Takeaway'), ('6', 'Prayer Room');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m6-1', '6', 'Gurame Bakar', 'Ikan gurame dibakar dengan bumbu manis gurih khas Cianjur.', 98000, 'https://images.unsplash.com/photo-1580456108502-866418d184f4?w=800', 'Food', true),
('m6-2', '6', 'Nasi Liwet', 'Nasi gurih dimasak dalam panci kastrol dengan ikan teri.', 45000, 'https://images.unsplash.com/photo-1634626132717-38df374d284e?w=800', 'Food', true),
('m6-3', '6', 'Tumis Kangkung Terasi', 'Sayuran kangkung segar ditumis dengan terasi harum.', 28000, 'https://images.unsplash.com/photo-1563294320-f47225bd04ac?w=800', 'Food', false);

-- Seribu Rasa (7)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('7', 'Seribu Rasa', 'Cita rasa kuliner Asia Tenggara dan Indonesia yang dikemas dalam nuansa elegan.', 'Southeast Asian', 'Menteng, Jakarta', 'Jl. H. Agus Salim No. 128, Menteng, Jakarta Pusat', '+62 21 392 8892', 'menteng@seriburasa.com', 'expensive', 4.8, 1800, 200);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('7', 'https://images.unsplash.com/photo-1514361892635-6b07e31e75f9?w=800'), ('7', 'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800'), ('7', 'https://images.unsplash.com/photo-1581349485608-9469926a8e5e?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('7', 'monday', '11:00', '22:00'), ('7', 'tuesday', '11:00', '22:00'), ('7', 'wednesday', '11:00', '22:00'), ('7', 'thursday', '11:00', '22:00'), ('7', 'friday', '11:00', '22:00'), ('7', 'saturday', '11:00', '22:00'), ('7', 'sunday', '11:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('7', 'Private Room'), ('7', 'Bar'), ('7', 'Seafood Specialist'), ('7', 'Business Dining');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m7-1', '7', 'Gulai Kepala Ikan', 'Kepala ikan kakap dimasak dalam kuah gulai kental.', 180000, 'https://images.unsplash.com/photo-1614984288414-b1eb217e17cb?w=800', 'Food', true),
('m7-2', '7', 'Black Pepper Crab', 'Kepiting segar dimasak dengan saus lada hitam pedas.', 250000, 'https://images.unsplash.com/photo-1585250954930-58f707f1d467?w=800', 'Food', true),
('m7-3', '7', 'Thai Mango Salad', 'Salad mangga muda dengan dressing asam pedas segar.', 65000, 'https://images.unsplash.com/photo-1506459345638-765ed9f31525?w=800', 'Food', false);

-- Gudeg Yu Djum (8)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('8', 'Gudeg Yu Djum', 'Legenda kuliner Yogyakarta sejak 1951. Gudeg kering dengan rasa manis gurih.', 'Javanese', 'Yogyakarta', 'Jl. Wijilan No. 167, Panembahan, Yogyakarta', '+62 274 370 381', 'info@gudegyudjum.com', 'cheap', 4.6, 4500, 80);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('8', 'https://images.unsplash.com/photo-1626202133285-f37dd782415c?w=800'), ('8', 'https://images.unsplash.com/photo-1505253668822-420429a3d4be?w=800'), ('8', 'https://images.unsplash.com/photo-1568271714652-5a2139bc62c1?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('8', 'monday', '06:00', '22:00'), ('8', 'tuesday', '06:00', '22:00'), ('8', 'wednesday', '06:00', '22:00'), ('8', 'thursday', '06:00', '22:00'), ('8', 'friday', '06:00', '22:00'), ('8', 'saturday', '06:00', '22:00'), ('8', 'sunday', '06:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('8', 'Legendary'), ('8', 'Souvenir'), ('8', 'Traditional'), ('8', 'Fast Service');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m8-1', '8', 'Nasi Gudeg Komplit', 'Nasi dengan gudeg, krecek, telur, dan suwir ayam.', 45000, 'https://images.unsplash.com/photo-1626202133285-f37dd782415c?w=800', 'Food', true),
('m8-2', '8', 'Ayam Opor Bagian Paha', 'Ayam opor bumbu kuning yang empuk.', 35000, 'https://images.unsplash.com/photo-1603083561556-9e8a735392bd?w=800', 'Food', true),
('m8-3', '8', 'Teh Poci Gula Batu', 'Teh wangi melati disajikan di poci tanah liat.', 15000, 'https://images.unsplash.com/photo-1564770178496-51e442971206?w=800', 'Drink', false);

-- Bandar Djakarta (9)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('9', 'Bandar Djakarta', 'Pasar ikan segar di pinggir laut. Pilih sendiri ikan, udang, kepiting hidup.', 'Seafood', 'Ancol, Jakarta', 'Pintu Timur Taman Impian Jaya Ancol, Jakarta Utara', '+62 21 645 5472', 'reservation@bandar-djakarta.com', 'moderate', 4.5, 5100, 500);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('9', 'https://images.unsplash.com/photo-1553184620-3b28b5c1cb2d?w=800'), ('9', 'https://images.unsplash.com/photo-1621348122709-0d322b649d28?w=800'), ('9', 'https://images.unsplash.com/photo-1596627685789-53b925b42605?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('9', 'monday', '11:00', '23:00'), ('9', 'tuesday', '11:00', '23:00'), ('9', 'wednesday', '11:00', '23:00'), ('9', 'thursday', '11:00', '23:00'), ('9', 'friday', '11:00', '23:30'), ('9', 'saturday', '10:00', '23:30'), ('9', 'sunday', '10:00', '23:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('9', 'Live Seafood'), ('9', 'Ocean View'), ('9', 'Outdoor Seating'), ('9', 'Live Music');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m9-1', '9', 'Kepiting Saus Padang', 'Kepiting hidup dimasak dengan saus padang yang pedas nendang.', 320000, 'https://images.unsplash.com/photo-1553184620-3b28b5c1cb2d?w=800', 'Food', true),
('m9-2', '9', 'Udang Peci Bakar Madu', 'Udang bakar dengan olesan madu dan lemon.', 150000, 'https://images.unsplash.com/photo-1606132646638-3f5af769974c?w=800', 'Food', true),
('m9-3', '9', 'Cumi Goreng Tepung', 'Cumi ring digoreng renyah dengan saus tartar.', 85000, 'https://images.unsplash.com/photo-1605493666373-162d142d7637?w=800', 'Food', false);

-- Kampung Daun (10)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('10', 'Kampung Daun', 'Menikmati hidangan Sunda di dalam saung privat di lembah hutan.', 'Sundanese', 'Bandung', 'Jl. Sersan Bajuri No. 88, Cihideung, Bandung', '+62 22 278 7915', 'info@kampungdaun.id', 'moderate', 4.7, 3800, 400);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('10', 'https://images.unsplash.com/photo-1445964047600-cdbdb873673d?w=800'), ('10', 'https://images.unsplash.com/photo-1625937759425-63402e86d009?w=800'), ('10', 'https://images.unsplash.com/photo-1605333190886-5d63be538466?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('10', 'monday', '10:00', '22:00'), ('10', 'tuesday', '10:00', '22:00'), ('10', 'wednesday', '10:00', '22:00'), ('10', 'thursday', '10:00', '22:00'), ('10', 'friday', '10:00', '23:00'), ('10', 'saturday', '09:00', '23:00'), ('10', 'sunday', '09:00', '22:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('10', 'Nature View'), ('10', 'Private Saung'), ('10', 'Romantic'), ('10', 'Cool Climate');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m10-1', '10', 'Nasi Timbel Komplit', 'Nasi bungkus daun pisang, ayam goreng, tahu tempe, sambal.', 65000, 'https://images.unsplash.com/photo-1629854445391-7d4d03d3c809?w=800', 'Food', true),
('m10-2', '10', 'Surabi Durian', 'Pancake tradisional Bandung dengan saus durian.', 30000, 'https://images.unsplash.com/photo-1598214886806-c87b84b7078b?w=800', 'Dessert', true),
('m10-3', '10', 'Bajigur', 'Minuman santan hangat dengan gula aren dan jahe.', 25000, 'https://images.unsplash.com/photo-1588661730030-a355606d2890?w=800', 'Drink', false);

-- Merah Putih (11)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('11', 'Merah Putih', 'Eksperimen masakan Indonesia klasik and modern di bangunan megah.', 'Modern Indonesian', 'Seminyak, Bali', 'Jl. Petitenget No. 100X, Kerobokan, Bali', '+62 361 8465950', 'info@merahputihbali.com', 'expensive', 4.9, 2100, 180);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('11', 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800'), ('11', 'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800'), ('11', 'https://images.unsplash.com/photo-1544148103-0773bf10d330?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('11', 'monday', '12:00', '00:00'), ('11', 'tuesday', '12:00', '00:00'), ('11', 'wednesday', '12:00', '00:00'), ('11', 'thursday', '12:00', '00:00'), ('11', 'friday', '12:00', '00:00'), ('11', 'saturday', '12:00', '00:00'), ('11', 'sunday', '12:00', '00:00');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('11', 'Architecture'), ('11', 'Cocktail Bar'), ('11', 'Vegetarian Options'), ('11', 'Valet');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m11-1', '11', 'Babi Guling', 'Suckling pig khas Bali dengan kulit renyah.', 220000, 'https://images.unsplash.com/photo-1628108985172-e56580f4f9f7?w=800', 'Food', true),
('m11-2', '11', 'Soft Shell Crab', 'Kepiting soka goreng dengan bumbu rujak.', 145000, 'https://images.unsplash.com/photo-1551608756-324df39c43d8?w=800', 'Food', true),
('m11-3', '11', 'Bali Martini', 'Cocktail khas dengan arak Bali dan buah tropis.', 120000, 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800', 'Drink', false);

-- Sarang Oci (12)
INSERT INTO restaurants (id, name, description, cuisine, location, address, phone, email, price_range, rating, review_count, capacity)
VALUES ('12', 'Sarang Oci', 'Cita rasa asli Manado yang pedas dan segar.', 'Manadonese', 'Jakarta Selatan', 'Jl. Bulungan No. 22, Blok M, Jakarta Selatan', '+62 21 722 0000', 'info@sarangoci.com', 'moderate', 4.6, 1400, 90);

INSERT INTO restaurant_images (restaurant_id, image_url) VALUES ('12', 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800'), ('12', 'https://images.unsplash.com/photo-1615937657715-bc7b4b7962c1?w=800'), ('12', 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800');

INSERT INTO opening_hours (restaurant_id, day_of_week, open_time, close_time) VALUES ('12', 'monday', '10:00', '21:30'), ('12', 'tuesday', '10:00', '21:30'), ('12', 'wednesday', '10:00', '21:30'), ('12', 'thursday', '10:00', '21:30'), ('12', 'friday', '10:00', '22:00'), ('12', 'saturday', '10:00', '22:00'), ('12', 'sunday', '10:00', '21:30');

INSERT INTO restaurant_features (restaurant_id, feature) VALUES ('12', 'Spicy Food'), ('12', 'Halal'), ('12', 'Family Dining'), ('12', 'Authentic Taste');

INSERT INTO menu_items (id, restaurant_id, name, description, price, image_url, category, is_best_seller) VALUES
('m12-1', '12', 'Ekor Tenggiri Bakar', 'Ekor ikan tenggiri dibakar dengan bumbu rica.', 95000, 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800', 'Food', true),
('m12-2', '12', 'Perkedel Jagung', 'Gorengan jagung manis yang super renyah.', 35000, 'https://images.unsplash.com/photo-1615937657715-bc7b4b7962c1?w=800', 'Food', true),
('m12-3', '12', 'Es Brenebon', 'Es kacang merah khas Manado dengan susu cokelat.', 30000, 'https://images.unsplash.com/photo-1550614000-4b9519e072eb?w=800', 'Dessert', false);
