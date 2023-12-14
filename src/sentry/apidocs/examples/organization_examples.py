from drf_spectacular.utils import OpenApiExample


class OrganizationExamples:
    LIST_PROJECTS = [
        OpenApiExample(
            "Success",
            value=[
                {
                    "dateCreated": "2018-11-06T21:19:58.536Z",
                    "firstEvent": None,
                    "access": [],
                    "hasAccess": True,
                    "id": "3",
                    "isBookmarked": False,
                    "isMember": True,
                    "name": "Prime Mover",
                    "platform": "",
                    "platforms": [],
                    "slug": "prime-mover",
                    "team": {
                        "id": "2",
                        "name": "Powerful Abolitionist",
                        "slug": "powerful-abolitionist",
                    },
                    "teams": [
                        {
                            "id": "2",
                            "name": "Powerful Abolitionist",
                            "slug": "powerful-abolitionist",
                        }
                    ],
                    "environments": ["local"],
                    "eventProcessing": {"symbolicationDegraded": False},
                    "features": ["releases"],
                    "firstTransactionEvent": True,
                    "hasSessions": True,
                    "hasProfiles": True,
                    "hasReplays": True,
                    "hasMinifiedStackTrace": False,
                    "hasMonitors": True,
                    "hasCustomMetrics": False,
                    "hasUserReports": False,
                    "latestRelease": None,
                }
            ],
            status_codes=["200"],
            response_only=True,
        )
    ]

    RETRIEVE_EVENT_COUNTS_V2 = [
        OpenApiExample(
            "Successful response",
            value={
                "start": "2022-02-14T19:00:00Z",
                "end": "2022-02-28T18:03:00Z",
                "intervals": ["2022-02-28T00:00:00Z"],
                "groups": [
                    {
                        "by": {"outcome": "invalid"},
                        "totals": {"sum(quantity)": 165665},
                        "series": {"sum(quantity)": [165665]},
                    }
                ],
            },
            status_codes=["200"],
            response_only=True,
        ),
    ]

    RETRIEVE_SUMMARY_EVENT_COUNT = [
        OpenApiExample(
            "Get event counts for projects in an organization",
            value={
                "start": "2023-09-19T13:00:00Z",
                "end": "2023-09-19T12:28:00Z",
                "projects": [
                    {
                        "id": "1",
                        "slug": "android-project",
                        "stats": [
                            {
                                "category": "error",
                                "outcomes": {
                                    "accepted": 1930571,
                                    "filtered": 1934881,
                                    "rate_limited": 2506132,
                                    "invalid": 0,
                                    "abuse": 1938113,
                                    "client_discard": 1942414,
                                },
                                "totals": {"dropped": 2506132, "sum(quantity)": 10252111},
                            },
                            {
                                "category": "transaction",
                                "outcomes": {
                                    "accepted": 1909849,
                                    "filtered": 1947142,
                                    "rate_limited": 2458946,
                                    "invalid": 0,
                                    "abuse": 1927179,
                                    "client_discard": 1931595,
                                },
                                "totals": {"dropped": 2458946, "sum(quantity)": 10174711},
                            },
                        ],
                    },
                ],
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    UPDATE_ORG_MEMBER = [
        OpenApiExample(
            "Update Successful",
            value={
                "id": "57377908164",
                "email": "sirpenguin@antarcticarocks.com",
                "name": "Sir Penguin",
                "user": {
                    "id": "280094367316",
                    "name": "Sir Penguin",
                    "username": "sirpenguin@antarcticarocks.com",
                    "email": "sirpenguin@antarcticarocks.com",
                    "avatarUrl": "https://secure.gravatar.com/avatar/16aeb26c5fdba335c7078e9e9ddb5149?s=32&d=mm",
                    "isActive": True,
                    "hasPasswordAuth": True,
                    "isManaged": False,
                    "dateJoined": "2021-07-06T21:13:58.375239Z",
                    "lastLogin": "2021-08-02T18:25:00.051182Z",
                    "has2fa": False,
                    "lastActive": "2021-08-02T21:32:18.836829Z",
                    "isSuperuser": False,
                    "isStaff": False,
                    "experiments": {},
                    "emails": [
                        {
                            "id": "2153450836",
                            "email": "sirpenguin@antarcticarocks.com",
                            "is_verified": True,
                        }
                    ],
                    "avatar": {"avatarType": "letter_avatar", "avatarUuid": None},
                    "authenticators": [],
                    "canReset2fa": True,
                },
                "role": "member",
                "orgRole": "member",
                "roleName": "Member",
                "pending": False,
                "expired": False,
                "flags": {
                    "idp:provisioned": False,
                    "idp:role-restricted": False,
                    "sso:linked": False,
                    "sso:invalid": False,
                    "member-limit:restricted": False,
                    "partnership:restricted": False,
                },
                "dateCreated": "2021-07-06T21:13:01.120263Z",
                "inviteStatus": "approved",
                "inviterName": "maininviter@antarcticarocks.com",
                "teams": ["cool-team", "ancient-gabelers"],
                "teamRoles": [
                    {"teamSlug": "ancient-gabelers", "role": "admin"},
                    {"teamSlug": "powerful-abolitionist", "role": "contributor"},
                ],
                "invite_link": None,
                "isOnlyOwner": False,
                "orgRoleList": [
                    {
                        "id": "billing",
                        "name": "Billing",
                        "desc": "Can manage subscription and billing details.",
                        "scopes": ["org:billing"],
                        "allowed": True,
                        "isAllowed": True,
                        "isRetired": False,
                        "is_global": False,
                        "isGlobal": False,
                        "minimumTeamRole": "contributor",
                    },
                    {
                        "id": "member",
                        "name": "Member",
                        "desc": "Members can view and act on events, as well as view most other data within the organization.",
                        "scopes": [
                            "team:read",
                            "project:releases",
                            "org:read",
                            "event:read",
                            "alerts:write",
                            "member:read",
                            "alerts:read",
                            "event:admin",
                            "project:read",
                            "event:write",
                        ],
                        "allowed": True,
                        "isAllowed": True,
                        "isRetired": False,
                        "is_global": False,
                        "isGlobal": False,
                        "minimumTeamRole": "contributor",
                    },
                    {
                        "id": "admin",
                        "name": "Admin",
                        "desc": "Admin privileges on any teams of which they're a member. They can create new teams and projects, as well as remove teams and projects on which they already hold membership (or all teams, if open membership is enabled). Additionally, they can manage memberships of teams that they are members of. They cannot invite members to the organization.",
                        "scopes": [
                            "team:admin",
                            "org:integrations",
                            "project:admin",
                            "team:read",
                            "project:releases",
                            "org:read",
                            "team:write",
                            "event:read",
                            "alerts:write",
                            "member:read",
                            "alerts:read",
                            "event:admin",
                            "project:read",
                            "event:write",
                            "project:write",
                        ],
                        "allowed": True,
                        "isAllowed": True,
                        "isRetired": True,
                        "is_global": False,
                        "isGlobal": False,
                        "minimumTeamRole": "admin",
                    },
                    {
                        "id": "manager",
                        "name": "Manager",
                        "desc": "Gains admin access on all teams as well as the ability to add and remove members.",
                        "scopes": [
                            "team:admin",
                            "org:integrations",
                            "project:releases",
                            "team:write",
                            "member:read",
                            "org:write",
                            "project:write",
                            "project:admin",
                            "team:read",
                            "org:read",
                            "event:read",
                            "member:write",
                            "alerts:write",
                            "alerts:read",
                            "event:admin",
                            "project:read",
                            "event:write",
                            "member:admin",
                        ],
                        "allowed": True,
                        "isAllowed": True,
                        "isRetired": False,
                        "is_global": True,
                        "isGlobal": True,
                        "minimumTeamRole": "admin",
                    },
                    {
                        "id": "owner",
                        "name": "Owner",
                        "desc": "Unrestricted access to the organization, its data, and its settings. Can add, modify, and delete projects and members, as well as make billing and plan changes.",
                        "scopes": [
                            "team:admin",
                            "org:integrations",
                            "project:releases",
                            "org:admin",
                            "team:write",
                            "member:read",
                            "org:write",
                            "project:write",
                            "project:admin",
                            "team:read",
                            "org:read",
                            "event:read",
                            "member:write",
                            "alerts:write",
                            "org:billing",
                            "alerts:read",
                            "event:admin",
                            "project:read",
                            "event:write",
                            "member:admin",
                        ],
                        "allowed": True,
                        "isAllowed": True,
                        "isRetired": False,
                        "is_global": True,
                        "isGlobal": True,
                        "minimumTeamRole": "admin",
                    },
                ],
                "teamRoleList": [
                    {
                        "id": "contributor",
                        "name": "Contributor",
                        "desc": "Contributors can view and act on events, as well as view most other data within the team's projects.",
                        "scopes": [
                            "team:read",
                            "project:releases",
                            "org:read",
                            "event:read",
                            "member:read",
                            "alerts:read",
                            "project:read",
                            "event:write",
                        ],
                        "allowed": False,
                        "isAllowed": False,
                        "isRetired": False,
                        "isMinimumRoleFor": None,
                    },
                    {
                        "id": "admin",
                        "name": "Team Admin",
                        "desc": "Admin privileges on the team. They can create and remove projects, and can manage the team's memberships. They cannot invite members to the organization.",
                        "scopes": [
                            "team:admin",
                            "org:integrations",
                            "project:admin",
                            "team:read",
                            "project:releases",
                            "org:read",
                            "team:write",
                            "event:read",
                            "alerts:write",
                            "member:read",
                            "alerts:read",
                            "event:admin",
                            "project:read",
                            "event:write",
                            "project:write",
                        ],
                        "allowed": False,
                        "isAllowed": False,
                        "isRetired": False,
                        "isMinimumRoleFor": "admin",
                    },
                ],
            },
            status_codes=["200"],
            response_only=True,
        )
    ]
