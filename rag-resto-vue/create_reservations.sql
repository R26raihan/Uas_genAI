CREATE TABLE IF NOT EXISTS reservations (
    id VARCHAR(50) PRIMARY KEY,
    restaurant_id VARCHAR(50),
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    guests INTEGER NOT NULL,
    special_requests TEXT,
    status VARCHAR(20) DEFAULT 'confirmed',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX (id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
);

-- Dummy Data
INSERT INTO reservations (id, restaurant_id, customer_name, customer_email, customer_phone, date, time, guests, special_requests, status) VALUES
('res-1', '1', 'Budi Santoso', 'budi@example.com', '081234567890', CURRENT_DATE, '19:00:00', 4, 'Ulang tahun, minta meja dekat jendela', 'confirmed'),
('res-2', '1', 'Siti Aminah', 'siti@example.com', '089876543210', CURRENT_DATE, '20:00:00', 2, NULL, 'confirmed'),
('res-3', '2', 'John Doe', 'john@example.com', '081122334455', CURRENT_DATE + INTERVAL 1 DAY, '18:30:00', 6, 'Alergi kacang', 'confirmed'),
('res-4', '3', 'Dewi Lestari', 'dewi@example.com', '085566778899', CURRENT_DATE + INTERVAL 2 DAY, '12:00:00', 10, 'Booking ruang VIP', 'confirmed'),
('res-5', '1', 'Rahmat Hidayat', 'rahmat@example.com', '081299887766', CURRENT_DATE, '19:30:00', 2, NULL, 'cancelled');
