from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from sslcommerz_lib import SSLCOMMERZ
import uuid
from account.models import User
from rest_framework import status  
from django.conf import settings
from django.shortcuts import redirect
from advertisement.models import RentAdvertisement,RentRequest

class PaymentViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def create_payment(self, request):
        # SSLCommerz configuration
        settings = {
            'store_id': 'techn671e3a7c8eda9',
            'store_pass': 'techn671e3a7c8eda9@ssl',
            'issandbox': True
        }
        sslcz = SSLCOMMERZ(settings)

        # Generate unique transaction ID
        tran_id = str(uuid.uuid4())[:10].replace('-', '').upper()
        # Extract data from the request
        user_id = request.data.get('user')
        advertisement = request.data.get('advertisement')
        total_amount = request.data.get('total_amount', 00.00)
        currency = request.data.get('currency', "BDT")
        cus_name = request.data.get('cus_name', "test")
        cus_email = request.data.get('cus_email', "test@test.com")
        cus_phone = request.data.get('cus_phone', "01700000000")
        cus_add1 = request.data.get('cus_add1', "customer address")
        cus_city = request.data.get('cus_city', "Dhaka")
        cus_country = request.data.get('cus_country', "Bangladesh")

        # Define callback URLs
        success_url = request.build_absolute_uri(f'/payment/success/?tran_id={tran_id}&user_id={user_id}&advertisement={advertisement}')
        fail_url = request.build_absolute_uri(f'/payment/cancle/')
        fail_url = request.build_absolute_uri('/payment/fail/')
        cancel_url = request.build_absolute_uri('/payment/cancel/')
    

        # Create payment information
        post_body = {
            'total_amount': total_amount,
            'currency': currency,
            'tran_id': tran_id,
            'success_url': success_url,
            'fail_url': fail_url,
            'cancel_url': cancel_url,
            'emi_option': 0,
            'cus_name': cus_name,
            'cus_email': cus_email,
            'cus_phone': cus_phone,
            'cus_add1': cus_add1,
            'cus_city': cus_city,
            'cus_country': cus_country,
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test",
            'product_category': "Test Category",
            'product_profile': "general"
        }

        # Create payment session with SSLCommerz
        try:
            user=User.objects.get(id=user_id)
            response = sslcz.createSession(post_body)
            if response.get('status') == 'SUCCESS' and 'GatewayPageURL' in response:
                return Response({"url": response['GatewayPageURL']})
            return Response({"error": "Unable to create payment session"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['post'])
    def success(self, request):
        try:
            # Extract parameters
            user_id = request.query_params.get('user_id')
            tran_id = request.query_params.get('tran_id')
            advertisement_id = request.query_params.get('advertisement')
            
            # Get user and active cart items
            user = User.objects.get(id=user_id)
            advertisement=RentAdvertisement.objects.get(id=advertisement_id)
            RentRequest.objects.create(advertisement=advertisement,requester=user,is_accepted=True)
            advertisement.request_accepted=True
            advertisement.save()
    
            # return Response({"success": "BOOking"}, status=status.HTTP_200_OK)
            return redirect(settings.SUCCESS_URL)

        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def cancel(self, request):
        return redirect(settings.CANCLE_URL)
    
    @action(detail=False, methods=['post'])
    def fail(self, request):
        return redirect(settings.FAILED_URL)