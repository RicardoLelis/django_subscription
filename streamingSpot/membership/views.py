from django.shortcuts import render
from django.views import generic
from membership.models import Membership, UserMembership, Subscription


class MembershipView(generic.ListView):
    model = Membership
    template_name = 'membership/list.html'

    def get_user_membership(self):
        user_membership_qs = UserMembership.objects.filter(
            user=self.request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = self.get_user_membership(self.request)
        context['current_membership'] = str(current_membership)
        return context


class MembershipsView(generic.ListView):
    template_name = 'membership/memberships.html'
    context_object_name = 'membership_list'

    def get_queryset(self):
        """
        Returns all membership plans available 
        """
        return Membership.objects.all()


class UserMembershipsView(generic.ListView):
    template_name = 'membership/user_memberships.html'
    context_object_name = 'user_membership_list'

    def get_queryset(self):
        """
        Returns all user membership plans available 
        """
        return UserMembership.objects.all()


class SubscriptionsView(generic.ListView):
    template_name = 'membership/subscriptions.html'
    context_object_name = 'subscriptions_list'

    def get_queryset(self):
        """
        Returns all subscriptions available 
        """
        return Subscription.objects.all()
