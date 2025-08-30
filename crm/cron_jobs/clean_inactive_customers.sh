#!/bin/bash

# Run Django shell to delete inactive customers
deleted_count=$(python manage.py shell -c "
import datetime
from crm.models import Customer, Order

one_year_ago = datetime.date.today() - datetime.timedelta(days=365)

# Customers who have not placed any orders in the last year
inactive_customers = Customer.objects.exclude(
    id__in=Order.objects.filter(order_date__gte=one_year_ago).values('customer_id')
)

count = inactive_customers.count()
inactive_customers.delete()

print(count)
")

# Log the result with a timestamp
echo \"$(date '+%Y-%m-%d %H:%M:%S') - Deleted \$deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
