__all__ = [
    'BaseData',
    'InputData',
    'InternalData',
    'LocalData',
    'LocationData',
    'OutputData',
    'RelativeData',
]
import toloka.client.project.template_builder.base
import typing


class BaseDataMetaclass(toloka.client.project.template_builder.base.BaseTemplateMetaclass):
    @staticmethod
    def __new__(
        mcs,
        name,
        bases,
        namespace,
        **kwargs
    ): ...


class BaseData(toloka.client.project.template_builder.base.BaseComponent, metaclass=BaseDataMetaclass):
    """Components used for working with data: input, output, or intermediate.

    Attributes:
       path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
           path to the array element, specify its sequence number starting from zero, for example: items.0
       default: The value to be used as the default data. This value will be shown in the interface, so it might hide
           some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class BaseData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]


class InputData(BaseData):
    """The input data.

    For example, links to images that will be shown to Tolokers. In the Template Builder sandbox, you can
    set an example of input data.

    Attributes:
        path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
            path to the array element, specify its sequence number starting from zero, for example: items.0
        default: The value to be used as the default data. This value will be shown in the interface, so it might hide
            some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class InputData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]


class InternalData(BaseData):
    """The data available only from within the task.

    This data is not saved to the results. Use this data to calculate or store intermediate values.

    Attributes:
        path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
            path to the array element, specify its sequence number starting from zero, for example: items.0
        default: The value to be used as the default data. This value will be shown in the interface, so it might hide
            some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class InternalData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]


class LocalData(BaseData):
    """The local data available only from inside the component.

    This data is used in some auxiliary components, such as helper.transform.

    Attributes:
        path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
            path to the array element, specify its sequence number starting from zero, for example: items.0
        default: The value to be used as the default data. This value will be shown in the interface, so it might hide
            some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class LocalData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]


class LocationData(toloka.client.project.template_builder.base.BaseComponent):
    """This component sends the device coordinates

    To find out if the transmitted coordinates match the ones that you specified, use the conditions.DistanceConditionV1.
    """

    def __init__(self) -> None:
        """Method generated by attrs for class LocationData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class OutputData(BaseData):
    """The output data.

    This is what you get when you click the Send button.

    Attributes:
        path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
            path to the array element, specify its sequence number starting from zero, for example: items.0
        default: The value to be used as the default data. This value will be shown in the interface, so it might hide
            some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class OutputData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]


class RelativeData(BaseData):
    """A special component for saving data.

    It's only available in the field.list component.

    Attributes:
        path: Path to the property containing data. Dots are used as separators: path.to.some.element. To specify the
            path to the array element, specify its sequence number starting from zero, for example: items.0
        default: The value to be used as the default data. This value will be shown in the interface, so it might hide
            some placeholders, for example, in the field.text component.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Any] = None,
        default: typing.Optional[typing.Any] = None
    ) -> None:
        """Method generated by attrs for class RelativeData.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    path: typing.Optional[typing.Any]
    default: typing.Optional[typing.Any]
