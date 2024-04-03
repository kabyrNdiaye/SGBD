import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="opencart"
)

cur = conn.cursor()

def TotalCustomers():
    cur.execute("SELECT COUNT(*) AS total_customers FROM oc_customer")
    return cur.fetchone()
def TotalSales():
    cur.execute("SELECT SUM(total) AS total_sales FROM oc_order")
    return cur.fetchone()

def PeopleOnline():
    cur.execute("SELECT COUNT(*) AS connected_clients FROM oc_session WHERE expire > NOW()")
    return cur.fetchone()

def TotalTransactions():
    cur.execute("SELECT COUNT(*) AS total_transactions FROM oc_order WHERE order_status_id IN (1,2,3,4)")
    return cur.fetchone()

def BlockAllTransactions():
    cur.execute("UPDATE oc_order SET order_status_id = X WHERE order_status_id NOT IN (X)")
    conn.commit()

def UniqueVisitorsPerPeriod(period):
    if period == 'day':
        cur.execute("SELECT DATE(date_added) AS date, COUNT(DISTINCT ip) AS unique_visitors FROM oc_customer_online GROUP BY DATE(date_added)")
    elif period == 'week':
        cur.execute("SELECT YEARWEEK(date_added) AS week, COUNT(DISTINCT ip) AS unique_visitors FROM oc_customer_online GROUP BY YEARWEEK(date_added)")
    elif period == 'month':
        cur.execute("SELECT DATE_FORMAT(date_added, '%Y-%m') AS month, COUNT(DISTINCT ip) AS unique_visitors FROM oc_customer_online GROUP BY DATE_FORMAT(date_added, '%Y-%m')")
    return cur.fetchall()

def MostVisitedPages():
    cur.execute("SELECT COUNT(*) AS visits, url FROM oc_customer_online GROUP BY url ORDER BY visits DESC LIMIT 10")
    return cur.fetchall()

def MostUsedBrowsers():
    cur.execute("SELECT COUNT(*) AS visits, SUBSTRING_INDEX(SUBSTRING_INDEX(referer, ' ', 2), ' ', -1) AS browser FROM oc_customer_online GROUP BY browser ORDER BY visits DESC")
    return cur.fetchall()

def RegionsByVisitors():
    cur.execute("SELECT COUNT(*) AS visits, SUBSTRING_INDEX(SUBSTRING_INDEX(referer, '/', 3), '/', -1) AS region FROM oc_customer_online WHERE referer IS NOT NULL GROUP BY region ORDER BY visits DESC")
    return cur.fetchall()

def TrafficSources():
    cur.execute("SELECT COUNT(*) AS visits, referer FROM oc_customer_online WHERE referer IS NOT NULL GROUP BY referer ORDER BY visits DESC")
    return cur.fetchall()

def PeakAccessTimes():
    cur.execute("SELECT HOUR(date_added) AS hour, COUNT(*) AS visits FROM oc_customer_online GROUP BY HOUR(date_added) ORDER BY visits DESC")
    return cur.fetchall()

def MostActiveUsers():
    cur.execute("SELECT COUNT(*) AS activity, customer_id FROM oc_customer_online GROUP BY customer_id ORDER BY activity DESC")
    return cur.fetchall()

def AveragePageLoadTime():
    # Ce calcul nécessite des outils de monitoring spécifiques en plus des requêtes SQL
    pass

def FrequentAccessErrors():
    cur.execute("SELECT COUNT(*) AS errors_404 FROM oc_url_alias WHERE `query` LIKE '%404%'")
    return cur.fetchone()

def ReferringSites():
    cur.execute("SELECT COUNT(*) AS visits, referer FROM oc_customer_online WHERE referer IS NOT NULL GROUP BY referer ORDER BY visits DESC")
    return cur.fetchall()

def TotalOrders():
    cur.execute("SELECT COUNT(*) AS total_orders FROM oc_order")
    return cur.fetchone()

def TotalRevenue():
    cur.execute("SELECT SUM(total) AS total_revenue FROM oc_order")
    return cur.fetchone()

def BestSellingProducts():
    cur.execute("SELECT p.product_id, pd.name AS product_name, SUM(op.quantity) AS total_sold FROM oc_order_product op JOIN oc_product p ON op.product_id = p.product_id JOIN oc_product_description pd ON p.product_id = pd.product_id GROUP BY op.product_id ORDER BY total_sold DESC LIMIT 10")
    return cur.fetchall()

def AverageOrderAmount():
    cur.execute("SELECT AVG(total) AS average_order_amount FROM oc_order")
    return cur.fetchone()

def ConversionRate():
    cur.execute("SELECT COUNT(*) AS total_orders, COUNT(DISTINCT customer_id) AS total_customers, (COUNT(*) / COUNT(DISTINCT customer_id)) AS conversion_rate FROM oc_order")
    return cur.fetchone()

def NewCustomersToday():
    cur.execute("SELECT COUNT(*) AS new_customers FROM oc_customer WHERE DATE(date_added) = CURDATE()")
    return cur.fetchone()

def TotalProductsInStock():
    cur.execute("SELECT COUNT(*) AS total_products_in_stock FROM oc_product WHERE quantity > 0")
    return cur.fetchone()

def OutOfStockProducts():
    cur.execute("SELECT COUNT(*) AS out_of_stock_products FROM oc_product WHERE quantity = 0")
    return cur.fetchone()

def VisitsPerDay():
    cur.execute("SELECT DATE(date_added) AS date, COUNT(*) AS total_visits FROM oc_customer_online GROUP BY DATE(date_added)")
    return cur.fetchall()

def PagesPerVisit():
    cur.execute("SELECT ROUND(COUNT(*) / COUNT(DISTINCT ip), 2) AS pages_per_visit FROM oc_customer_online")
    return cur.fetchone()

def AverageSessionDuration():
    cur.execute("SELECT ROUND(AVG(TIMESTAMPDIFF(MINUTE, date_added, expire)), 2) AS avg_session_duration FROM oc_session")
    return cur.fetchone()

def BounceRate():
    cur.execute("SELECT COUNT(*) AS single_page_visits FROM oc_customer_online WHERE referer IS NULL")
    return cur.fetchone()

def OrdersByPaymentMethod():
    cur.execute("SELECT payment_method, COUNT(*) AS total_orders FROM oc_order GROUP BY payment_method")
    return cur.fetchall()

def OrdersByShippingMethod():
    cur.execute("SELECT shipping_method, COUNT(*) AS total_orders FROM oc_order GROUP BY shipping_method")
    return cur.fetchall()

def OrdersByStatus():
    cur.execute("SELECT os.name AS status_name, COUNT(*) AS total_orders FROM oc_order o JOIN oc_order_status os ON o.order_status_id = os.order_status_id GROUP BY o.order_status_id")
    return cur.fetchall()
