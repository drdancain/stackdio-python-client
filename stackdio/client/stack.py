# -*- coding: utf-8 -*-

# Copyright 2014,  Digital Reasoning
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .exceptions import StackException
from .http import HttpMixin, get, post, put, delete
from .version import deprecated


class StackMixin(HttpMixin):
    VALID_LOG_TYPES = {
        'provisioning': ['log', 'err'],
        'global-orchestration': ['log', 'err'],
        'orchestration': ['log', 'err'],
        'launch': ['log'],
    }

    @post('stacks/')
    def create_stack(self, stack_data):
        """Launch a stack as described by stack_data"""
        return stack_data

    @get('stacks/', paginate=True)
    def list_stacks(self):
        """Return a list of all stacks"""
        pass

    @get('stacks/{stack_id}/')
    def get_stack(self, stack_id):
        """Get stack info"""
        pass

    @get('stacks/', paginate=True)
    def search_stacks(self, **kwargs):
        """Search for stacks that match the given criteria"""
        pass

    @delete('stacks/{stack_id}/')
    def delete_stack(self, stack_id):
        """Destructively delete a stack forever."""
        pass

    @get('stacks/{stack_id}/action/')
    def get_valid_stack_actions(self, stack_id):
        pass

    @get_valid_stack_actions.response
    def get_valid_stack_actions(self, resp):
        return resp['available_actions']

    @post('stacks/{stack_id}/action/')
    def do_stack_action(self, stack_id, action):
        """Execute an action on a stack"""
        valid_actions = self.get_valid_stack_actions(stack_id)

        if action not in valid_actions:
            raise StackException('Invalid action, must be one of %s' %
                                 ', '.join(valid_actions))

        return {'action': action}

    @get('stacks/{stack_id}/history/', paginate=True)
    def get_stack_history(self, stack_id):
        """Get stack info"""
        pass

    @get('stacks/{stack_id}/hosts/', paginate=True)
    def get_stack_hosts(self, stack_id):
        """Get a list of all stack hosts"""
        pass

    @get('stacks/{stack_id}/logs/{log_type}.{level}.{date}', jsonify=False)
    def get_logs(self, stack_id, log_type, level='log', date='latest', tail=None):
        """Get logs for a stack"""

        if log_type and log_type not in self.VALID_LOG_TYPES:
            raise StackException('Invalid log type, must be one of %s' %
                                 ', '.join(self.VALID_LOG_TYPES.keys()))

        if level not in self.VALID_LOG_TYPES[log_type]:
            raise StackException('Invalid log level, must be one of %s' %
                                 ', '.join(self.VALID_LOG_TYPES[log_type]))

    @get('stacks/{stack_id}/security_groups/', paginate=True)
    def list_access_rules(self, stack_id):
        """
        Get Access rules for a stack
        :rtype: list
        """
        pass

    @deprecated
    def get_access_rule_id(self, stack_id, title):
        """Find an access rule id"""

        rules = self.list_access_rules(stack_id)

        try:
            for group in rules:
                if group.get('blueprint_host_definition').get('title') == title:
                    return group.get('id')
        except TypeError:
            pass

        raise StackException('Access Rule %s not found' % title)

    @get('security_groups/{group_id}/rules/', paginate=True)
    def list_rules_for_group(self, group_id):
        pass

    @put('security_groups/{group_id}/rules/')
    def edit_access_rule(self, group_id, data=None):
        """Add an access rule to a group"""
        return data
