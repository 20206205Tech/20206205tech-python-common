from loguru import logger
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def init_tracing(
    service_name: str,
    honeycomb_api_key: str,
    endpoint: str = "https://api.honeycomb.io/v1/traces",
):
    """
    Initializes OpenTelemetry tracing with Honeycomb exporter.

    Args:
        service_name: Name of the service.
        honeycomb_api_key: Honeycomb API key.
        endpoint: Honeycomb OTLP endpoint.
    """
    # 1. Định nghĩa Resource (Tên service)
    resource = Resource.create({SERVICE_NAME: service_name})

    # 2. Cấu hình OTLP Exporter gửi đến Honeycomb
    exporter = OTLPSpanExporter(
        endpoint=endpoint,
        headers={"x-honeycomb-team": honeycomb_api_key},
    )

    # 3. Thiết lập Provider và Processor
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)

    # Đăng ký provider toàn cục
    trace.set_tracer_provider(provider)
    logger.info(f"✅ Tracing initialized for {service_name}")
